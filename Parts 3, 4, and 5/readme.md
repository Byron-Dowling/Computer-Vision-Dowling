# Report

## Project Overview
  - For my project, we are wanting to train a model to spot the difference between a situation on the road that a human driver would consider to be dangerous.
  - Essentially, any situation that a driver would either proceed with caution or be ready to brake at a moment's notice because of sudden changing variables.
  - Examples that have been annotated include:
    - Railroad crossings
    - Pedestrians walking in the middle of the road
    - Pedestrians in the crosswalk when it "is not their turn to walk"
    - Construction areas
    - Open doors and or cars blocking the roadway
    - Delivery vehicles in the process of loading/unloading

## Image Data
  - Sourced from: https://www.crcv.ucf.edu/data/GMCP_Geolocalization/
  - Amir Roshan Zamir and Mubarak Shah, "Image Geo-localization Based on Multiple Nearest Neighbor Feature Matching using Generalized Graphs", IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), 2014
  - Stored here on my Google Drive: https://drive.google.com/file/d/1thSCTsoo0Q7m7pVqIHiitSFdoND5uX6h/view?usp=sharing

## Choice of Classifer
  - Since the aspect of a dangerous driving situation is subjective, it appears to be a good problem to utilize current XAI techniques
  - As a result, we are pitting traditional Cross-Entropy machine learning vs CYBORG loss to determine if the annotations supported in CYBORG will not only outperform Cross-Entropy, but also give a level of trust and assurance as the annotations have been collected by human interpretations of the driving situation presented in the imagery.
  - The way CYBORG works is that it is a final loss function within the neural network architecture that takes the regions that the model has deemed salient to the decision and weighs this against the annotation regions that our human annotators have deemed to be salient.
    - CYBORG will evaluate these differences and penalizes the models for large differences between the model's salience and the annotation region.
    - This prevents potential trust issues where perhaps within an image, the human annotator highlighted a pedestrian, but the cross entropy model highlighted some area within a tree on the sidewalk
    - Essentially it helps steer the model to learn the features that are most important, according to humans, for the decision

## Classification Accuracy
  - My Training Loss reported was minimal on my XENT model over 100 epochs
    - However the performance was mixed and I am currently tweaking some paramters
    - The current performance showed a 100% success rate on test data of images whose labels were "Not Dangerous"
    - However, the model failed to accurately classify a single dangerous situation as "Dangerous"
    - This gave a total testing accuracy of 71% and this is mainly because of the ratio of test data selected and is a reflection of the likelihood of seeing dangerous situations in the dataset
    - Running XENT at 50 epochs instead of 100 yielded the same results
  - CYBORG is still in progress

## Commentary
  - Close to being done but not 100% yet
