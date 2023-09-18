"""
    Student:    Byron Dowling
    Class:      Computer Vision (CSE 60535)
    Term:       University of Notre Dame, Fall 2023

    In this example, we will simulate an "invisibility cloak" using a static
    background, color detection and segmentation. 

    The key idea is to replace the current frame pixels corresponding to
    the cloth with the background pixels to generate the effect of an 
    invisibility cloak. 
    
    The basic concepts are:
        1. Capture and store the background frame.
        2. Detect the colored cloth using a color detection algorithm
        3. Segment out the colored cloth by generating a mask.
        4. Generate the final augmented output to create the magical effect.

"""

import cv2
import numpy as np
import time

# Open the webcam
cap = cv2.VideoCapture(0)

# We give some time for the camera to setup
time.sleep(3)
background = 0
final_output = 0
res_scale = 0.5

# First, we need to capture and store the static background frame
while (cap.isOpened()):
    retval, bgr = cap.read()

    cv2.imshow("Background", bgr)

    action = cv2.waitKey(1)
    # type s to exit the while loop after background has been detected after
    # for example 10-15 seconds
    if action == ord('s'):
        background = bgr
        break
    
    # closing the windows selects the last frame as the background
    cv2_ver = cv2.__version__.split('.')[0]
        
    if cv2_ver == '3':
        if cv2.getWindowProperty("Background", 0) == -1:
            background = bgr
            break
    if cv2_ver == '4':
        if cv2.getWindowProperty("Background", cv2.WND_PROP_VISIBLE) <= 0:
            background = bgr
            break


# And here the magic happens
while(cap.isOpened()):
    ret, bgr = cap.read()
    if not ret:
        break

	# Converting the color space from BGR to HSV
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    
    #######################################################
    """
        HSV Values for my Green-ish "cloak"
            - Hue: 102-110
            - Saturation: 62-122
            - Value: 160-235

            and

            - Hue: 102-110
            - Saturation: 106-150
            - Value: 180-240
    """
    lower_hsv = np.array([102,62,160])
    upper_hsv = np.array([110,122,235])
    mask = cv2.inRange(hsv,lower_hsv,upper_hsv)

    # If you see more than one peak in either of the histograms, you can keep adding separate masks for all such peaks:
    lower_hsv = np.array([102,106,180])
    upper_hsv = np.array([110,150,240])
    mask2 = cv2.inRange(hsv,lower_hsv,upper_hsv)
    mask = mask + mask2
    #######################################################

	# Refining the mask corresponding to the detected red color
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((13,13),np.uint8),iterations=3)
    mask = cv2.dilate(mask,np.ones((11,11),np.uint8),iterations = 1)
    cv2.imshow("Final mask", mask)

    # Now we need to replace the pixel values of the detected red color region with
    # corresponding pixel values of the static background and generate an
    # augmented output that converts our cloak into an invisibility cloak.
    
    #######################################################
    """
        ***TASK FOR YOU: 
        Use cv2.bitwise_and() function and your "mask" array to create an image 
        "res1" with pixel values equal to the pixel values of the static background
        within the detected invisible cloak region.
    """
    res1 = cv2.bitwise_and(background, background, mask=mask)
    cv2.imshow("res1", res1)
    #######################################################


    #######################################################
    """
        ***TASK FOR YOU: 
        Next, use cv2.bitwise_and() function again to "remove" (= make them black) from the webcam 
        stream ("bgr") all pixels found within the invisible cloak region; this will be "res2". 
        Tip: you may need to invert your mask array -- use cv2.bitwise_not() for this purpose.
    """
    mask = cv2.bitwise_not(mask)
    res2 = cv2.bitwise_and(bgr, bgr, mask=mask)
    cv2.imshow("res2", res2)
    #######################################################


    #######################################################
    """
        ***TASK FOR YOU: 
        Finally, combine "res1" and "res2" using cv2.addWeighted() function 
    """
    final_output = cv2.addWeighted(res1,1,res2,1,0)
    #######################################################


    cv2.imshow('Here the magic happens !!!',final_output)
    k = cv2.waitKey(10)
    if k & 0xFF == 27:
        break

    """
        My results were a little mixed. It defintely works, but I think the issue is more
        related to my choice of cloak which is a very light green and the level of lighting
        seemed to affect portion of the "cloak" to where they were not being detected and thus
        becoming invisible.

        It seems like every cloak-like item I have either has elaborate patterns or is plain
        black so I didn't have a lot of great options to pick from.
    """

    
cap.release()
cv2.destroyAllWindows()
