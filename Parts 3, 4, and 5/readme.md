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

## Annotations
- Individual JPG's can be accessed here: https://drive.google.com/drive/folders/1hWXhqZ4mQg1yhUIf9mXkibYBF0VVC7Sa?usp=sharing
- The annotations are highlighted areas within the image that I've deemed to be indicative of a dangerous situation
- More specifically, my interpretation of a dangerous situation is if I'm the driver in the photo, would I be "riding my brake" or ready at a moment's notice to stop my car in the event something happens.
- These were crafted using Label Studio and includes essentially "blank" annotations for images that are not deemed dangerous since technically the entire image would reference that decision

## Choice of Classifer
  - Since the aspect of a dangerous driving situation is subjective, it appears to be a good problem to utilize current XAI techniques
  - As a result, we are pitting traditional Cross-Entropy machine learning vs CYBORG loss to determine if the annotations supported in CYBORG will not only outperform Cross-Entropy, but also give a level of trust and assurance as the annotations have been collected by human interpretations of the driving situation presented in the imagery.
  - The way CYBORG works is that it is a final loss function within the neural network architecture that takes the regions that the model has deemed salient to the decision and weighs this against the annotation regions that our human annotators have deemed to be salient.
    - CYBORG will evaluate these differences and penalizes the models for large differences between the model's salience and the annotation region.
    - This prevents potential trust issues where perhaps within an image, the human annotator highlighted a pedestrian, but the cross entropy model highlighted some area within a tree on the sidewalk
    - Essentially it helps steer the model to learn the features that are most important, according to humans, for the decision

## Classification Accuracy
  ### Cross Entropy
  - My Training Loss reported was minimal on my XENT model over 100 epochs
    - However the performance was mixed and I am currently tweaking some parameters
    - The current performance showed a 100% success rate on test data of images whose labels were "Not Dangerous"
    - However, the model failed to accurately classify a single dangerous situation as "Dangerous"
    - This gave a total testing accuracy of 71% and this is mainly because of the ratio of test data selected and is a reflection of the likelihood of seeing dangerous situations in the dataset
    - Running XENT at 50 epochs instead of 100 yielded the same results
  - After tweaking the distribution of the training and validation data and starting out at 50 epochs, performance was better
    - Although training loss was still around 15%, performance was better in terms of being able to correctly identify both parameters
    - With a slight bias towards situations being more dangerous than not dangerous
    - Obviously this isn't going into production, but thinking more situations are dangerous than not isn't the worst thing in the world
    - On the latest run, 71% of Non-dangerous situations were correctly identified while 69% of Dangerous situations were identified
      
  ### CYBORG
  - CYBORG is "running" with the code available
  - However, I'm not seeing an increase in performance over Cross entropt as the baseline learning rate of between 71% - 78% classification success is not increasing with the use of CYBORG and its annotations.
  - I have tweaked the learning rate a few times and different epochs with minimal success.
  - At this point, I would say its still ambiguous if there is a combination that will achieve good performance or if this is an instance where CYBORG is not very successful on this type of data set

## Commentary
  - Cross Entropy didn't perform super great and this is no doubt due to a relatively small dataset compared to other experiments as we are training on roughly 1000 images.
  - CYBORG's strengths are smaller dataset and annotation sizes so it makes sense to try the experiment this way, but no doubt with more samples, Cross Entropy would perform a bit better, and with time I may be able to add more samples from my own driving into the sample pool.
  - I suspect one thing that could potentially be holding back CYBORG from learning is because of the ambiguity to what was annotated in certain images vs what was not annotated in other images.
    - For instance, there many instances where I did not annotate pedestrians in the cross walk because they were in the direction that the car could not legally turn into because of a one way street.
    - My hunch would be that the model still may be struggling to glean this road law context that I am considering when annotating the images, despite also annotating relevant street signs in the dangerous situations.
  - After more thought as well, if I were to design this general experiment again, and I didn't necessarily have to use CYBORG, I mwould probably do some sort of multi-hiearchial object detection.
    - Something like where there is lane detection, and then separate object detection layered over this, and then detect for objects, like cyclists or pedestrians, crossing over the lanes detected by the vehicle.
