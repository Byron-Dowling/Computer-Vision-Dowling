# Final Report
### Highlights:
 - Traditional Cross Entropy achieved a peak Training Accuracy of 78%
 - The CYBORG trained model achieve a peak Training Accuracy near 99%
 - CYBORG appears to be performing better both on testing and unseen data
 - CYBORG is occasionally showing a bias towards Non-Dangerous situations to be classified as Dangerous

## Files
|   #    | File                    | Description                                          |
| :---:  | ----------------------- | ---------------------------------------------------- |
|   1    | train_droid_alphas.py              | [Main Driver of the training process](https://github.com/Byron-Dowling/Computer-Vision-Dowling/blob/main/Part%205%20Final%20Report/train_droid_alphas.py)                             |
|   2    | test_droid_alpha.py      | [Script to run a test csv to test the final trained model](https://github.com/Byron-Dowling/Computer-Vision-Dowling/blob/main/Part%205%20Final%20Report/test_droid.py)  |
|   3    | dataset_loader_cam.py          | [Utility file to load the dataset](https://github.com/Byron-Dowling/Computer-Vision-Dowling/blob/main/Part%205%20Final%20Report/dataset_Loader_cam.py) |
|   4    | models.py                 | [Utility file that implements various model architectures](https://github.com/Byron-Dowling/Computer-Vision-Dowling/blob/main/Part%205%20Final%20Report/models.py)                      |
|   5    | current_CYBORG_model_100_epochs.pth                 | [CYBORG Model Click here to access](https://drive.google.com/file/d/1nybqKBVE8CWbdBnfAUj21g9gBlsDv4Uv/view?usp=sharing)                      |
|   6    | current_XENT_model_100_epochs.pth                  | [Cross Entropy Model Click hereto access](https://drive.google.com/file/d/1Ogg15uBovc1A-tDXYXoTr-oNu8jdw2hj/view?usp=sharing)                      |


## Dataset 
 - The dataset that I have trained and tested the model on is from Google Street View and consists of urban driving situations in New York City, Pittsburgh, Charlotte, and Orlando
 - The unseen data that I tested the model on is also sourced from Google Street View and is from either Denver CO, Fort Worth TX, or Dallas TX
 - The total images sourced for this experiment is 992 images
 - It was originally an even 1500 but several images were not correctly cropped as promised from the source and they did not accurately reflect the drivers' point of view in the image.
 - This however does give CYBORG an opportunity to show its strength as it works well with smaller data sets
 - The way my experiment is set up is to use a 70/30 training testing split so that 70% of the cumulative data is for training and the remaining 30% is reserved for testing.
 - The unseen data was simply a handful of images that were hand picked on my own accord.
 - Dataset sourced from: https://www.crcv.ucf.edu/data/GMCP_Geolocalization/
 - Amir Roshan Zamir and Mubarak Shah, "Image Geo-localization Based on Multiple Nearest Neighbor Feature Matching using Generalized Graphs", IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), 2014
 - Stored here on my Google Drive: https://drive.google.com/file/d/1thSCTsoo0Q7m7pVqIHiitSFdoND5uX6h/view?usp=sharing

## Annotations
- Individual JPG's can be accessed here: https://drive.google.com/drive/folders/1hWXhqZ4mQg1yhUIf9mXkibYBF0VVC7Sa?usp=sharing
- The annotations are highlighted areas within the image that I've deemed to be indicative of a dangerous situation
- More specifically, my interpretation of a dangerous situation is if I'm the driver in the photo, would I be "riding my brake" or ready at a moment's notice to stop my car in the event something happens.
- These were crafted using Label Studio and includes essentially "blank" annotations for images that are not deemed dangerous since technically the entire image would reference that decision
  
### Example Anotations:

<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/Annotations/Screenshot%202023-12-11%20at%2017-19-03%20Label%20Studio.png?raw=true" width = "550" height = "350"/>

<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/Annotations/Screenshot%20from%202023-12-11%2017-17-53.png?raw=true" width = "550" height = "350"/>


## Classification Accuracy on Testing Data: Cross Entropy Model
 - Prediction: **Not Dangerous**
 - Score: 0.33
 - Actual: ***Dangerous***
<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/000160_2.jpg" width = "550" height = "350"/>

 - Prediction: **Not Dangerous**
 - Score: 0.11
 - Actual: ***Not Dangerous***
<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/000004_2.jpg" width = "550" height = "350"/>

 - Prediction: **Not Dangerous**
 - Score: 0.30
 - Actual: ***Not Dangerous***
<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/000015_2.jpg" width = "550" height = "350"/>

 - Prediction: **Not Dangerous**
 - Score: 0.37
 - Actual: ***Dangerous***
<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/000052_2.jpg" width = "550" height = "350"/>

 - Prediction: **Not Dangerous**
 - Score: 0.45
 - Actual: ***Dangerous***
<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/000176_2.jpg" width = "550" height = "350"/>


## Classification Accuracy on Testing Data: CYBORG Model
 - Prediction: **Dangerous**
 - Score: 0.97
 - Actual: ***Dangerous***
<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/000160_2.jpg" width = "550" height = "350"/>

 - Prediction: **Not_Dangerous**
 - Score: 0.41
 - Actual: ***Not Dangerous***
<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/000004_2.jpg" width = "550" height = "350"/>

 - Prediction: **Dangerous**
 - Score: 0.56
 - Actual: ***Not Dangerous***
<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/000015_2.jpg" width = "550" height = "350"/>

 - Prediction: **Dangerous**
 - Score: 0.60
 - Actual: ***Dangerous***
<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/000052_2.jpg" width = "550" height = "350"/>

 - Prediction: **Dangerous**
 - Score: 0.97
 - Actual: ***Dangerous***
<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/000176_2.jpg" width = "550" height = "350"/>


## Classification Accuracy on Unseen Data: Cross Entropy
 - Prediction: **Not Dangerous**
 - Score: 0.36
 - Actual: ***Dangerous***
<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/Unseen_Data/unseen_1.jpg" width = "550" height = "350"/>

 - Prediction: **Not Dangerous**
 - Score: 0.08
 - Actual: ***Not Dangerous***
<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/Unseen_Data/unseen_3.jpg?raw=true" width = "550" height = "350"/>

 - Prediction: **Not Dangerous**
 - Score: 0.36
 - Actual: ***Dangerous***
<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/Unseen_Data/unseen_5.jpg?raw=true" width = "550" height = "350"/>

 - Prediction: **Not Dangerous**
 - Score: 0.04
 - Actual: ***Not Dangerous***
<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/Unseen_Data/unseen_4.jpg?raw=true" width = "550" height = "350"/>


## Classification Accuracy on Unseen Data: CYBORG
 - Prediction: **Dangerous**
 - Score: 0.79
 - Actual: ***Dangerous***
<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/Unseen_Data/unseen_1.jpg" width = "550" height = "350"/>

 - Prediction: **Not Dangerous**
 - Score: 0.24
 - Actual: ***Not Dangerous***
<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/Unseen_Data/unseen_3.jpg?raw=true" width = "550" height = "350"/>

 - Prediction: **Dangerous**
 - Score: 0.99
 - Actual: ***Dangerous***
<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/Unseen_Data/unseen_5.jpg?raw=true" width = "550" height = "350"/>

 - Prediction: **Not Dangerous**
 - Score: 0.08
 - Actual: ***Not Dangerous***
<img src="https://github.com/Byron-Dowling/Assets/blob/main/Driving_Test_Data/Unseen_Data/unseen_4.jpg?raw=true" width = "550" height = "350"/>


## Presentation Component:
 - Can be accessed here: https://drive.google.com/file/d/1yfmTwmc9xy8sP3maZbR_Rwhu8Yrdk_7X/view?usp=sharing
 - Same one that I'm showing for the demo final

## Further Testing:
 - You *should* be able to test the code from here: https://colab.research.google.com/drive/15QoncZ1S7azSlWwFqvMwq9jpHCuoXo7v?authuser=2#scrollTo=LvslFRVNGrKn
 - You will need a copy of one of the Torch Models on Google Drive
 - A csv with the links to unseen images to test
 - I'm not entirely sure how to make all the files already be available in the Colab Notebook since I've been connecting my Google Drive account to store things that are too large to attach.
