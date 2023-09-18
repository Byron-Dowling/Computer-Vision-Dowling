"""
    Student:    Byron Dowling
    Class:      Computer Vision (CSE 60535)
    Term:       University of Notre Dame, Fall 2023

    Practical Tasks and Comments/Answers:

        Task 2A:
            - Select one object that you want to track and set the RGB
              channels to the selected ranges (found by colorSelection.py).

            - Check if HSV color space works better. Can you ignore one or two
              channels when working in HSV color space? Why?
                NOTE
                - HSV tendeded to work better than RGB in my experiments

                - Yes you can ignore channels when working in HSV and it is the basis for doing
                  image segmentation such as finding curves within an image or dividing an image
                  down to its objects.

                - Doing a little bit of digging, I see many explanations citing HSV being able to 
                  separate color from intensity, and this lines up with my experiences in this
                  assignment so far. In fact, I think the best example is when using BGR for tracking
                  red objects vs HSV for red objects. BGR kept recognizing parts of my hair and skin
                  as red objects, whereas HSV tended to be more accurate in only finding objects closely
                  related. This was also evident when I tried detecting a bright red bag of chips vs the
                  more maroon-ish red of the M&M and the chip bag was only identified in the right lighting.

            - Try to track candies of different colors (blue, yellow, green).
                NOTE
                - I was able to accomplish this by creating a class that simply required the
                  input numpy arrays with the proper ranges and to pass in the image and mask.

        Task 2B:
            - Adapt your code to track multiple objects of *the same* color simultaneously, 
              and show them as separate objects in the camera stream.
                NOTE
                - Done by Looping through the contours

        Task 2C:
            - Adapt your code to track multiple objects of *different* colors simultaneously,
              and show them as separate objects in the camera stream. Make your code elegant 
              and requiring minimum changes when the number of different objects to be detected increases.
                NOTE
                - I did this by creating a class with methods to do most of the contouring

                - This way all we need to do is create a new object with the specified RGB or HSV values
                  and we can add its method calls into the main loop and display those colors.

        Task for students attending 60000-level course:
            - Choose another color space (e.g., LAB or YCrCb), modify colorSelection.py, select color ranges 
              and after some experimentation say which color space was best (RGB, HSV or the additional one you selected).
                NOTE
                - LAB performed even better than HSV which I had noted above was outperforming BGR
                - In particular, LAB seemed to be the most accurate at finding the exact shade of the colors
                  expressed in my numpy arrays so in my tests it seemed to mostly find just the M&M's

            - Try to explain the reasons why the selected color space performed best. 
                NOTE
                - The LAB color space has one channel dedicated entirely to brightness compared to BGR/RGB where the
                  brightness for each channel is accounted into each one.
                
                - I've seen the LAB color space described as most similar to how we as humans perceive color and that
                  it can separate close shades of color the same way we can with the human eye but may appear very similar
                  in another color spacee. I think this advantage is why it seemed to be the most accurate at detecting 
                  just the colors I selected and not too much in the background.
"""

import cv2  
import numpy as np


###################################################################################################
## Simple object to pair bounds and masks to color-defined objects
class CV_Object :
    def __init__(self,LB=None,UB=None,Color=None,CS="BGR",OM=None,DB=False,image=None):
        self.image = image
        self.lowerBound = LB
        self.UpperBound = UB
        self.ObjectMask = OM
        self.Debugging = DB;
        self.Color = Color
        self.minObjectSize = 20;
        self.HSV_Mask = None
        self.LAB_Mask = None
        self.HSV = False
        self.BGR = False
        self.LAB = False

        ## Color Space defaults to BGR if no value is passed in
        self.ColorSpace = CS

        if self.ColorSpace == "BGR":
            self.BGR = True
        elif self.ColorSpace == "HSV":
            self.HSV = True
        else: 
            self.LAB = True
    
    def updateImage(self, image):
        self.image = image

    def updateMask(self):
        if self.HSV:
            self.HSV_Mask = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
            self.ObjectMask = cv2.inRange(self.HSV_Mask, self.lowerBound, self.UpperBound)
        if self.BGR:
            self.ObjectMask = cv2.inRange(self.image, self.lowerBound, self.UpperBound)
        if self.LAB:
            self.LAB_Mask = cv2.cvtColor(self.image, cv2.COLOR_BGR2LAB)
            self.ObjectMask = cv2.inRange(self.LAB_Mask, self.lowerBound, self.UpperBound)
    
    def processContours(self):
        # Find connected components
        cc = cv2.connectedComponents(self.ObjectMask)
        ccimg = cc[1].astype(np.uint8)

        # Find contours of these objects
        contours, hierarchy = cv2.findContours(ccimg,
                                                    cv2.RETR_TREE,
                                                    cv2.CHAIN_APPROX_SIMPLE)[-2:]
        """
            We are using [-2:] to select the last two return values from the above function 
            to make the code work with both opencv3 and opencv4. This is because opencv3 provides
            3 return values but opencv4 discards the first.

            You may display the contour points if you want:
            cv2.drawContours(img, contours, -1, (0,255,0), 3)

            Loop through the contours found and display rects around 
            all matches instead of just one.
        """
        for contour in contours:
            # Draw a rectangle around the contour
            x, y, w, h = cv2.boundingRect(contour)

            # Do not show very small objects
            if w > self.minObjectSize or h > self.minObjectSize:
                cv2.rectangle(self.image, (x, y), (x+w, y+h), (0,255,0), 3)
                cv2.putText(self.image,            # image
                f"{self.Color} object!",        # text
                (x, y-10),                  # start position
                cv2.FONT_HERSHEY_SIMPLEX,   # font
                0.7,                        # size
                (0, 255, 0),                # BGR color
                1,                          # thickness
                cv2.LINE_AA)                # type of line

        if self.Debugging:
            self.DebugMode()


    def DebugMode(self):
        cv2.imshow(f"Binary image for {self.Color}", self.ObjectMask)
        """
            Resulting binary image may have large number of small objects.
            You may check different morphological operations to remove these unnecessary
            elements. You may need to check your ROI defined in step 1 to
            determine how many pixels your object may have.
        """
        kernel = np.ones((5,5), np.uint8)
        objmask = cv2.morphologyEx(self.ObjectMask, cv2.MORPH_CLOSE, kernel=kernel)
        objmask = cv2.morphologyEx(self.ObjectMask, cv2.MORPH_DILATE, kernel=kernel)
        cv2.imshow(f"{self.Color} Image after morphological operations", objmask)

###################################################################################################

"""
 ███╗   ███╗ █████╗ ██╗███╗   ██╗
 ████╗ ████║██╔══██╗██║████╗  ██║
 ██╔████╔██║███████║██║██╔██╗ ██║
 ██║╚██╔╝██║██╔══██║██║██║╚██╗██║
 ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
 ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝                     
"""
if __name__ == '__main__':
    cam = cv2.VideoCapture(0)

    """
        Defined Color Ranges obtained using ColorSelction.py:
            Blue:
                BGR = [84,45,8] to [240,180,40]
                HSV = [97,150,80] to [112,255,220]
                LAB = [66,88,28] to [215,193,105]

            Green:
                BGR = [8,54,0] to [60,195,70]
                HSV = [5,95,50] to [68,255,180]
                LAB = [120,78,132] to [172,90,149]

            Red:
                BGR = [24,24,59] to [82,60,126]
                HSV = [166,130,60] to [179,175,123]
                LAB = [70,179,124] to [132,204,162]
    """
    lower_blue_BGR = np.array([84,45,8])
    upper_blue_BGR = np.array([240,180,40])
    lower_blue_HSV = np.array([97,150,80])
    upper_blue_HSV = np.array([112,255,220])
    lower_blue_LAB = np.array([66,88,28])
    upper_blue_LAB = np.array([215,193,105])

    lower_green_BGR = np.array([8,54,0])
    upper_green_BGR = np.array([60,195,70])
    lower_green_HSV = np.array([5,95,50])
    upper_green_HSV = np.array([68,255,180])
    lower_green_LAB = np.array([120,78,132])
    upper_green_LAB = np.array([172,90,149])

    lower_red_BGR = np.array([24, 24, 59])
    upper_red_BGR = np.array([82, 60, 126])
    lower_red_HSV = np.array([166,130,60])
    upper_red_HSV = np.array([179,175,123])
    lower_red_LAB = np.array([70,179,124])
    upper_red_LAB = np.array([132,204,162])

    """
        BGR Color-Space Objects
        Declared them here so we only have to update values instead of redeclaring
        the objects inside of the loop.
    """
    # BlueObject = CV_Object(lower_blue_BGR, upper_blue_BGR,"Blue","BGR")
    # GreenObject = CV_Object(lower_green_BGR, upper_green_BGR,"Green","BGR")
    # RedObject = CV_Object(lower_red_BGR, upper_red_BGR,"Red","BGR")

    """
        HSV Color-Space Objects
        Declared them here so we only have to update values instead of redeclaring
        the objects inside of the loop.
    """
    # BlueObject = CV_Object(lower_blue_HSV, upper_blue_HSV,"Blue","HSV")
    # GreenObject = CV_Object(lower_green_HSV, upper_green_HSV,"Green","HSV")
    # RedObject = CV_Object(lower_red_HSV, upper_red_HSV,"Red","HSV")

    """
        LAB Color-Space Objects
        Declared them here so we only have to update values instead of redeclaring
        the objects inside of the loop.
    """
    BlueObject = CV_Object(lower_blue_LAB, upper_blue_LAB,"Blue","LAB")
    GreenObject = CV_Object(lower_green_LAB, upper_green_LAB,"Green","LAB")
    RedObject = CV_Object(lower_red_LAB, upper_red_LAB,"Red","LAB")


    while (True):
        retval, img = cam.read()

        # rescale selfthe input image if it's too large
        res_scale = 0.5 
        img = cv2.resize(img, (0,0), fx = res_scale, fy = res_scale)

        ## For HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


        """
            Code for a blue object using BGR, HSV, or LAB

                - On this example, I noticed that the HSV seemed to identify the objects
                more easily and from a greater distance than BGR.

                - Adiitionally, the debugging imagery (binary and morphological operations) 
                showed much clearer silouhettes than when using BGR
        """
        ## Blue Object
        BlueObject.updateImage(img)
        BlueObject.updateMask()


        """
            Code for a green object using BGR, HSV, or LAB

                - On this example, I noticed that the HSV seemed to identify too many
                objects, not necessarily incorrectly, but it found the green paint on the
                wall here in my office, as well as finding traces of green in my jersey.

                - BGR on the other hand was more precisely finding just the M&M's and a smaller
                section of the green paint on the wall in the background
        """
        ## Green Object
        GreenObject.updateImage(img)
        GreenObject.updateMask()


        """
            Code for a red object using BGR, HSV, or LAB

                - On this example, I noticed that using BGR, the camera detected plenty of red
                in my hair and facial hair (which is fairly accurate) but still properly detected
                multiple red M&M's

                - HSV on the other hand here did not have background detection on things like my hair
                however, it only detected the M&M's when I got very close and it had difficulties 
                detecting them at an angle or if they were not directly in front of the camera.
        """
        ## Red Object
        RedObject.updateImage(img)
        RedObject.updateMask()


        ## If you want Debugging or not
        BlueObject.Debugging = True
        GreenObject.Debugging = True
        RedObject.Debugging = True

        ## Process the contours of each color object
        BlueObject.processContours()
        GreenObject.processContours()
        RedObject.processContours()

        cv2.imshow("Live WebCam", img)

        action = cv2.waitKey(1)
        if action & 0xFF == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

###################################################################################################
