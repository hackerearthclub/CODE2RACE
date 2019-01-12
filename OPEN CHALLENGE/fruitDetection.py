'''
*Functions: requiredFruitsTable(),count(),size(),OrangeCheck(),appleCheck(),blueberrycheck()
*Global Variables: sa,ma,la,sb,mb,lb,so,mo,lo,readVal
'''
from __future__ import print_function
import cv2
import numpy as np
import time
import serial

global readVal

sa = 0
ma = 0
la = 0
so = 0
mo = 0
lo = 0
sb = 0
mb = 0
lb = 0

open('/dev/ttyUSB0')
ser = serial.Serial('/dev/ttyUSB0', 9600)

''' 
*Function Name: requiredFruitsTable 
*Input: None
*Output: this function returns a list of required fruits to be picked when called 
*Logic: we enter the data from the required fruits table directly to the variable requiredFruits 
*Example Call: if x in requiredFruitsTable()
'''


def requiredFruitsTable():
    requiredFruits = ["medium orange", "medium orange", "medium blueberry", "medium apple", "small blueberry",
                      "small apple",
                      "large apple", "large blueberrry"]

    return requiredFruits


'''
*Function Name: count()
*Input: it inputs a string value containing fruit names
*Output: this function gives the number of fruit of each type and size collected
*Logic: when it receives the fruit string , it compares it with every condition and increments the value of the fruit it matches 
*Example Call: count(fruit) '''


def count(x):
    global sa

    global ma

    global la

    global so

    global mo

    global lo

    global sb

    global mb

    global lb

    if x == "small apple":
        sa += 1

    if x == "medium apple":
        ma += 1

    if x == "large apple":
        la += 1

    if x == "small blueberry":
        sb += 1

    if x == "medium blueberry":
        mb += 1

    if x == "large blueberry":
        lb += 1

    if x == "small orange":
        so += 1

    if x == "medium orange":
        mo += 1

    if x == "large orange":
        lo += 1


'''
*Function Name: size()
*Input: it takes in a float value and prints the size of the fruit according to it
*Output: it gives fruit size
*Logic: when size(x) is called, it checks in which range x falls and gives size according to it 
*Example Call: print size() 
'''


def size(x):
    if 20.0 < x < 2700.0:

        return "small"

    elif x > 2700.0 and x < 10000.0:

        return "medium"

    elif x > 10000.0:

        return "large"

    else:

        return "not detected"


'''
*Function Name: Orangecheck()
*Input: it takes an image as an input and checks whether orange is in it
*Output: it returns orange with its size if it is present in image
*Logic: it inputs an hsv image and masks it with the range of orange colour.
        It then checks the size of orange detected by using contours  
*Example Call: o=Orangecheck()'''


def Orangecheck(x):
    kernel = np.ones((5, 5), np.uint8)

    lower_orange = np.array([3, 100, 100])

    upper_orange = np.array([17, 255, 255])

    maskO = cv2.inRange(x, lower_orange, upper_orange)

    finmaskO = cv2.morphologyEx(maskO, cv2.MORPH_OPEN, kernel)

    cv2.imshow("finMask", finmaskO)

    image, contours, hierarchy = cv2.findContours(finmaskO, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:

        area = cv2.contourArea(cnt)

        # print area

        orangeSize = size(area)

        if orangeSize != "not detected":
            fruit = orangeSize + " orange"

        ser.write(b'o')

        time.sleep(1)

        return fruit

    # elif orangeSize == "not detected":

    return "not detected"


'''
*Function Name: appleCheck()
*Input: it takes an image as an input and checks whether apple is in it
*Output: it returns apple with its size if it is present in image
*Logic: it inputs an hsv image and masks it with the range of red colour.
        It then checks the size of appple detected by using contours  
*Example Call: a=appleCheck()'''


def appleCheck(x):
    kernel = np.ones((5, 5), np.uint8)

    lower_apple = np.array([0, 5, 5])

    upper_apple = np.array([12, 255, 255])

    maskR = cv2.inRange(x, lower_apple, upper_apple)

    finmaskR = cv2.morphologyEx(maskR, cv2.MORPH_OPEN, kernel)

    cv2.imshow("finMask", finmaskR)

    image, contours, hierarchy = cv2.findContours(finmaskR, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:

        area = cv2.contourArea(cnt)

        # print area

        appleSize = size(area)

        if appleSize != "not detected":

            fruit = appleSize + " apple"

            return fruit

        elif appleSize == "not detected":

            return "not detected"


'''
*Function Name: blueberrycheck()
*Input: it takes an image as an input and checks whether blueberry is in it
*Output: it returns blueberry  if it is present in image
*Logic: it inputs an hsv image and masks it with the range of blue colour.
*Example Call: b=blueberrycheck()'''


def blueberrycheck(x):
    kernel = np.ones((5, 5), np.uint8)

    lower_blue = np.array([90, 20, 20])

    upper_blue = np.array([150, 255, 255])

    maskB = cv2.inRange(x, lower_blue, upper_blue)

    finmaskB = cv2.morphologyEx(maskB, cv2.MORPH_OPEN, kernel)

    cv2.imshow("finMask", finmaskB)

    whiteArea = cv2.countNonZero(finmaskB)

    if whiteArea != 0:

        fruit = " blueberry"

        ser.write(b'b')

        time.sleep(1)

    elif whiteArea == 0:

        fruit = "not detected"

        ser.write(b'a')

        time.sleep(1)

    return fruit


while (True):
    '''working on a video feed is very processor hungry. it is inefficient and laggy when done on raspberry pi.
    to improve the accuracy of the code, we are capturing the frames and working on them , only when the firebird reaches node.
    when firebird reaches a node, it sends a value which is readby using ser.read()'''

    readValue = ser.read()

    while (readValue == "c"):

        time.sleep(1)

        cap = cv2.VideoCapture(0)
        ret, img = cap.read()
        cv2.imshow("frame", img)
        '''
        in this code the size detection is done using black and white thresholding. 
        first the image is converted to grayscale. then it is converted to binary image to detect contours 
        '''
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # newgray uses median blur to remove noise and define countours of fruit better
        newGray = cv2.medianBlur(gray, 31)

        retval, threshold = cv2.threshold(newGray, 75, 255, cv2.THRESH_BINARY)

        fin1Threshold = cv2.bitwise_not(threshold)

        kernel = np.ones((9, 9), np.uint8)
        finThreshold = cv2.morphologyEx(fin1Threshold, cv2.MORPH_OPEN, kernel)

        cv2.imshow("fin", finThreshold)

        image, contours, hierarchy = cv2.findContours(finThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(img, contours, 0, (80, 200, 55), 4)

        for cnt in contours:  # area
            area = cv2.contourArea(cnt)
            print(area)
            fruitSize = size(area)

            """
            we can not use orange to detect from this method. this is because in gray scale 
            its threshold is similar to some of the shadows obtained in the background
            """
        WhitePix = cv2.countNonZero(finThreshold)
        imageToCheck = hsv

        if WhitePix == 0 and Orangecheck(imageToCheck) != "not detected":
            fruit = Orangecheck(hsv)
        if WhitePix == 0 and Orangecheck(imageToCheck) == "not detected":
            fruit = "no fruit"
        if WhitePix != 0 and blueberrycheck(hsv) != "not detected":
            fruit = fruitSize + blueberrycheck(hsv)
        if WhitePix != 0 and blueberrycheck(hsv) == "not detected" and appleCheck(hsv) != "not detected":
            fruit = appleCheck(hsv)
        if WhitePix != 0 and blueberrycheck(hsv) == "not detected" and appleCheck(hsv) == "not detected":
            fruit = "no fruit"
        if fruit in requiredFruitsTable():
            print(fruit)
            count(fruit)

        cap.release()
        cv2.destroyAllWindows()
        break

    if readValue == "q":
        break

print("no of small apples:" + str(sa))

print("no of medium apples:" + str(ma))

print("no of large apples:" + str(la))

print("no of small blueberry:" + str(sb))

print("no of medium blueberry:" + str(mb))

print("no of large blueberry:" + str(lb))

print("no of small oranges:" + str(so))

print("no of medium oranges:" + str(mo))

print("no of large oranges:" + str(lo))

