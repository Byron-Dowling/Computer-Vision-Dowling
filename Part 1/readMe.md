# Recognition of Dangerous Driving Situations

### Overview
The goal of this project is to detect a dangerous driving situation that could potentially factor into the decision making of a semi-autonomous vehicle. Examples of these situations include:
  - pedestrians walking on sidewalks near the road
  - cars sticking out in the roadway
  - emergency vehicles
  - vehicles stopped on the shoulder
  - people approaching a cross walk
These are situations that us human drivers are familiar with, and when we see these events unfolding in real-time, we anticipate the potential of these events occuring and adjust our driving behavior accordingly. However, many autonomous vehicle prototypes still have trouble predicting the unfolding of these situations and instead are very reactionary in their processing of information. The goal of this project is to not only work on a solution to this problem, but provide an explainable component to the process by utilizing human annotations in the learning process.

### Technical Details

#### Datasets
To start, we will need some type of drive data dataset with your typical mundane urban driving. Some potential candidates include:
  - Waymo Perception Dataset: https://waymo.com/open/download/
  - nuScenes: https://www.nuscenes.org/
  - KITTI-360: https://www.cvlibs.net/datasets/kitti-360/
  - Audi Autonomous Driving Dataset: https://www.a2d2.audi/a2d2/en/dataset.html
    
#### Annotations
Once we have a healthy sample of images from standard driving situations, the idea is to collect annotations from actual US drivers and have them annotate any regions within the image that is a potential danger or is a situation that should factor into the decision making of the driver. We will need several 100's of these so we may look into getting some outside assistance on making these annotations. Additionally the annotations are very important because the actual thing being tracked is very abstract and requires context that can only initially be provided by humans. It's not just object tracking in that we're tracking pedestrians, or vehicles, or proximity to them, but it's all of these combined in a particular situation that a human has deemed as a potentially dangerous sitation. 

#### Models
Once we have these annotations collected, the goal of this experiment would be to run them through a normal cross-entropy trained model and compare that performance to the same annotations through a model using CYBORG loss. For those unfamiliar, CYBORG loss is a way to encourage a model to look at image regions that have been judged to be salient by humans. Because of this, the hypothesis would be to see how well CYBORG may perform over traditional cross entropy with these human annotated images. Additionally, CYBORG tends to not need as much input images and annotations as other models so it seems like a good choice for this project.

#### Testing
To test the model, we can save some of the input dataset images for testing. However, if this shows good success, I also have a raspberry pi and webcam rig at my disposal and I may be able to rig this up as a sort-of dash cam to where I could run this while doing my normal every day driving and see what type of data it would collect and record.
