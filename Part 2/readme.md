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
      - Current issue with this is that it already has bounding box labels
      - Trying to see if there is a set here without this information
  - nuScenes: https://www.nuscenes.org/
      - Unable to get an extracted copy of the dataset
  - KITTI-360: https://www.cvlibs.net/datasets/kitti-360/
      - Doesn't seem like the type of data we'll need
  - Audi Autonomous Driving Dataset: https://www.a2d2.audi/a2d2/en/dataset.html
      - Seems promising except that it's German-based roads and there could be an issue as to whether this translates well to US roads where we would test
