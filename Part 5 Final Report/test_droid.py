"""
    Name:   Byron Dowling
    Class:  Computer Vision
    Term:   Fall 2023

    @NOTE
        - This file is used to run and test a csv of testing samples, score the samples,
          and write the results to a csv output file.
"""
import sys
import torch
import torchvision.models as models
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
import glob
import os
import csv
import numpy as np
import argparse
from tqdm import tqdm
import matplotlib.pyplot as plt
sys.path.append("../")
from models import model_selection
import random

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # device = torch.device('cpu')
    device = torch.device('cuda')
    # parser.add_argument('-imageFolder', default=r'C:\Users\byron\OneDrive\Documents\Python Stuff\Computer Vision\Driving_Project\\',type=str)
    parser.add_argument('-imageFolder', default=r'C:\Users\byron\OneDrive\Documents\Python Stuff\Computer Vision\Driving_Project\Unseen_Test_Data\\',type=str)
    parser.add_argument('-modelPath',  default=r'C:\Users\byron\OneDrive\Documents\Python Stuff\Computer Vision\Driving_Project\Logs\current_CYBORG_model_100_epochs.pth',type=str)
    # parser.add_argument('-modelPath',  default=r'C:\Users\byron\OneDrive\Documents\Python Stuff\Computer Vision\Driving_Project\Logs\current_XENT_model_100_epochs.pth',type=str)
    # parser.add_argument('-csv',  default=r"C:\Users\byron\OneDrive\Documents\Python Stuff\Computer Vision\Driving_Project\testing_unseen.csv",type=str)
    parser.add_argument('-csv',  default=r"C:\Users\byron\OneDrive\Documents\Python Stuff\Computer Vision\Driving_Project\testing.csv",type=str)
    parser.add_argument('-outputPath', required=False, default= r'C:\Users\byron\OneDrive\Documents\Python Stuff\Computer Vision\Driving_Project\\',type=str)
    # parser.add_argument('-output_filename', default="scores_unseen_XENT_100eps.csv",type=str)
    parser.add_argument('-output_filename', default="scores.csv",type=str)
    parser.add_argument('-network',  default="densenet",type=str)
    parser.add_argument('-noSample', action='store_true')
    parser.add_argument('-fakeToken', default='Spoof', type=str)
    parser.add_argument('-sampleFactor',default=0.00835,type=float)
    parser.add_argument('-realSampleFactor',default=0.167,type=float)
    parser.add_argument('-nClasses',default=2,type=int)
    args = parser.parse_args()

    # seed random
    random.seed(1234)

    # Load weights of single binary DesNet121 model
    weights = torch.load(args.modelPath,map_location=torch.device('cpu'))
    if args.network == "resnet":
        im_size = 224
        model = models.resnet50(pretrained=True)
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, args.nClasses)
    elif args.network == "inception":
        im_size = 299
        model = models.inception_v3(pretrained=True,aux_logits=False)
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, args.nClasses)
    elif args.network == "xception":
        im_size = 299
        model, *_ = model_selection(modelname='xception', num_out_classes=args.nClasses)
    else: # else DenseNet
        im_size = 224
        model = models.densenet121(pretrained=True)
        num_ftrs = model.classifier.in_features
        model.classifier = nn.Linear(num_ftrs, args.nClasses)
    
    model.load_state_dict(weights['state_dict'])
    model = model.to(device)
    model.eval()

    if args.network == "xception":
        # Transformation specified for the pre-processing
        transform = transforms.Compose([
                    transforms.Resize([im_size, im_size]),
                    transforms.ToTensor(),
                    transforms.Normalize([0.5]*3, [0.5]*3)
                ])
    else:
        # Transformation specified for the pre-processing
        transform = transforms.Compose([
                    transforms.Resize([im_size, im_size]),
                    transforms.ToTensor(),
                    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
                ])

    imagesScores=[]
    sigmoid = nn.Sigmoid()

    imageCSV = open(args.csv,"r")
    for entry in tqdm(imageCSV):

        print(entry)

        tokens = entry.split(",")
        if tokens[0] != 'test':
            continue

        if not args.noSample:

            # take random sample
            if  (args.fakeToken in tokens[1] and random.random() > args.sampleFactor) or (
                 args.fakeToken not in tokens[1] and random.random() > args.realSampleFactor):
                continue

        upd_name = tokens[-1].replace("\n","")
        # upd_name = upd_name.replace(upd_name.split(".")[-1],"png")
        imgFile = args.imageFolder + upd_name

        # Read the image
        image = Image.open(imgFile).convert('RGB')
        # Image transformation
        tranformImage = transform(image)
        image.close()

        tranformImage = tranformImage[0:3,:,:].unsqueeze(0)
        tranformImage = tranformImage.to(device)

        # Output from single binary CNN model
        with torch.no_grad():
            output = model(tranformImage)

        PAScore = sigmoid(output).detach().cpu().numpy()[:, 1]
        SMScore = nn.Softmax(dim=1)(output).detach().cpu().numpy()[:, 1]
        imagesScores.append([imgFile, PAScore[0], SMScore[0]])

    # Writing the scores in the csv file
    with open(os.path.join(args.outputPath,args.output_filename),'w',newline='') as fout:
        writer = csv.writer(fout)
        writer.writerows(imagesScores)

