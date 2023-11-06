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
After running into trouble with the previous mentioned datasets, we're going to use the Google Streetview car dataset that is available at the link below. We are going to focus only on the images that are the foward facing view of the vehicle and the street view nature especially as this data set is from Pittsburgh, Orlando, and Manhatten, it should contain plenty of urban driving scenarios for our annotation collection. 
  - https://www.crcv.ucf.edu/data/GMCP_Geolocalization/
