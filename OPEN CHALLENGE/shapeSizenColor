
#classes and subclasses to import
import cv2
import numpy as np
import os
import math


def writecsv(color,shape,size,count):
    #open csv file in append mode
    global filename
    filep = open('results1B_943.csv','a')
    # create string data to write per image
    datastr = "," + color + "-" + shape + "-" + size + "-" + str(count)
    #write to csv
    filep.write(datastr)

def main(path):

    contours = {}
    approx = []
    scale = 0.5                                                                                                         #setting font size for text
    list = []                                                                                                           #creating an empty list

    def angle(pt1, pt2, pt0):                                                                                           #function to calculate angle for the shape
        dx1 = pt1[0][0] - pt0[0][0]
        dy1 = pt1[0][1] - pt0[0][1]
        dx2 = pt2[0][0] - pt0[0][0]
        dy2 = pt2[0][1] - pt0[0][1]
        return float((dx1 * dx2 + dy1 * dy2)) / math.sqrt(float((dx1 * dx1 + dy1 * dy1)) * (dx2 * dx2 + dy2 * dy2) + 1e-10)

    image = path                                                                                                        #selecting image from the path
    frame = cv2.imread(image)                                                                                           #reading the image
    list.append(image)                                                                                                  #appeding image in the list
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                                                                      #converting the image to grayscale

    canny = cv2.Canny(frame, 200, 200)                                                                                  #canny edge detection
    kernel = np.ones([5, 5], "uint8")                                                                                   #creating numpy array

    lower_blue = np.array([250, 0, 0])                                                                                  #lower threshold for blue color
    upper_blue = np.array([255, 10, 10])                                                                                #upper theshold for blue color
    mask_blue = cv2.inRange(frame, lower_blue, upper_blue)                                                              #setting the threshold range for blue mask
    mask_blue = cv2.dilate(mask_blue, kernel)                                                                           #masking for blue color

    lower_orange = np.array([0, 50, 200])                                                                               #lower threshold for orange color
    upper_orange = np.array([180, 200, 255])                                                                            #upper threshold for orange color
    mask_orange = cv2.inRange(frame, lower_orange, upper_orange)                                                        #setting the threshold range for orange mask
    mask_orange = cv2.dilate(mask_orange, kernel)                                                                       #masking for orange color

    lower_red = np.array([0, 0, 250])                                                                                   #lower threshold for red color
    upper_red = np.array([10, 10, 255])                                                                                 #upper threshold for red color
    mask_red = cv2.inRange(frame, lower_red, upper_red)                                                                 #setting the threshold range for red
    mask_red = cv2.dilate(mask_red, kernel)                                                                             #masking for orange color

    lower_green = np.array([0, 250, 0])                                                                                 #lower threshold for green color
    upper_green = np.array([10, 255, 10])                                                                               #upper threshold for green color
    mask_green = cv2.inRange(frame, lower_green, upper_green)                                                           #setting the threshold range for green
    mask_green = cv2.dilate(mask_green, kernel)                                                                         #making for green color

    lower_yellow = np.array([0, 200, 240])                                                                              #lower threshold for yellow color
    upper_yellow = np.array([5, 255, 255])                                                                              #upper threshold for yellow color
    mask_yellow = cv2.inRange(frame, lower_yellow, upper_yellow)                                                        #setting the threshold range for yellow
    mask_yellow = cv2.dilate(mask_yellow, kernel)                                                                       #making for yellow color

    canny2, contours, hierarchy = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)               #contour detection for blue color
    for i in range(0, len(contours)):                                                                                   #initiating the loop
        color = "blue"
        sq = 0
        cnt = contours[i]
        area = cv2.contourArea(cnt)                                                                                     #calculating area of contour
        approx = cv2.approxPolyDP(contours[i], cv2.arcLength(contours[i], True) * 0.04, True)                           #finding the vertices
        if (abs(cv2.contourArea(contours[i])) < 100 or not (cv2.isContourConvex(approx))):
            continue
        x, y, w, h = cv2.boundingRect(contours[i])
        if (len(approx) == 3):                                                                                          #logic for triangle
            shape = "triangle"
            if area <= 1585:                                                                                            #logic for size detection
                size = "small"
            elif area >= 5663:
                size = "large"
            else:
                size = "medium"

        elif (len(approx) == 4):                                                                                        #logic for four side polygon
            x, y, w, h = cv2.boundingRect(approx)
            ar = w / float(h)
            if ar >= 0.99 and ar <= 1.01:                                                                               #logic for square
                shape = "square"
                if area <= 2913:                                                                                        #logic for size detection
                    size = "small"
                elif area >= 10813:
                    size = "large"
                else:
                    size = "medium"

            else:                                                                                                       #logic for rectangle
                shape = "rectangle"
                if area <= 3993:                                                                                        #logic for size detection
                    size = "small"
                elif area >= 21213:
                    size = "large"
                else:
                    size = "medium"

        else:                                                                                                           #logic for circle
            area = cv2.contourArea(contours[i])
            radius = w / 2                                                                                              #calculating radius of circle
            if (abs(1 - (float(w) / h)) <= 2 and abs(1 - (area / (math.pi * radius * radius))) <= 0.2):
                shape = "circle"
                if area <= 2286:                                                                                        #logic for size detection
                    size= "small"
                elif area >= 8497:
                    size = "large"
                else:
                    size = "medium"
        cv2.putText(frame, color, (x + w / 3, y + h / 2), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), 1, cv2.LINE_AA)   #putting text color over image
        cv2.putText(frame, shape, (x + w / 3, y + (h / 2) + 15), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), 1,         #putting text shape over image
                    cv2.LINE_AA)

        for j in range(0, len(contours)):                                                                               #logic for similar images

            cnt = contours[j]
            area = cv2.contourArea(cnt)
            approx = cv2.approxPolyDP(contours[j], cv2.arcLength(contours[j], True) * 0.04, True)
            if (abs(cv2.contourArea(contours[j])) < 100 or not (cv2.isContourConvex(approx))):
                continue
            x, y, w, h = cv2.boundingRect(contours[j])
            if (len(approx) == 3):
                shape1 = "triangle"
                if area <= 1585:
                    size1 = "small"
                elif area >= 5663:
                    size1 = "large"
                else:
                    size1 = "medium"

            elif (len(approx) == 4):
                x, y, w, h = cv2.boundingRect(approx)
                ar = w / float(h)
                if ar >= 0.99 and ar <= 1.01:
                    shape1 = "square"
                    if area <= 2913:
                        size1 = "small"
                    elif area >= 10813:
                        size1 = "large"
                    else:
                        size1 = "medium"

                else:
                    shape1 = "rectangle"
                    if area <= 3993:
                        size1 = "small"
                    elif area >= 21213:
                        size1 = "large"
                    else:
                        size1 = "medium"

            else:
                area = cv2.contourArea(contours[j])
                radius = w / 2
                if (abs(1 - (float(w) / h)) <= 2 and abs(1 - (area / (math.pi * radius * radius))) <= 0.2):
                    shape1 = "circle"
                    if area <= 2286:
                        size1 = "small"
                    elif area >= 8497:
                        size1 = "large"
                    else:
                        size1 = "medium"
            if size1 == size and shape1 == shape:                                                                       #check number of similar number of images
                sq = sq + 1

        img = cv2.drawContours(frame, contours, -1, (0, 0, 0), 1)                                                       #drawing contours
        element = []                                                                                                    #creating  a sublist
        element.append(color + "-" + shape + "-" + size + "-" + str(sq))                                                #appending the shapes and colors in the list
        if element not in list:                                                                                         #removing repeated similar images
            list.append(element)                                                                                        #appending the sublist to the list
            writecsv(color, shape, size, sq)                                                                            #calling writecsv function


    canny2, contours, hierarchy = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)                #contour detection for red color
    for i in range(0, len(contours)):                                                                                   #initiating the loop
        color = "red"
        flag = 0
        cnt = contours[i]
        area = cv2.contourArea(cnt)                                                                                     #calculating area of contour
        approx = cv2.approxPolyDP(contours[i], cv2.arcLength(contours[i], True) * 0.04, True)                           #finding the vertices
        if (abs(cv2.contourArea(contours[i])) < 100 or not (cv2.isContourConvex(approx))):
            continue
        x, y, w, h = cv2.boundingRect(contours[i])
        if (len(approx) == 3):                                                                                          #logic for triangle
            shape = "triangle"
            if area <= 1585:                                                                                            #logic for size detection
                size = "small"
            elif area >= 5663:
                size = "large"
            else:
                size = "medium"

        elif (len(approx) == 4):                                                                                        #logic for shape having 4 sides
            x, y, w, h = cv2.boundingRect(approx)
            ar = w / float(h)
            if ar >= 0.99 and ar <= 1.01:                                                                               #logic for square
                shape = "square"
                if area <= 2913:                                                                                        #logic for size detection
                    size = "small"
                elif area >= 10813:
                    size = "large"
                else:
                    size = "medium"

            else:                                                                                                       #logic for rectangle
                shape = "rectangle"
                if area <= 3993:                                                                                        #logic for size detection
                    size = "small"
                elif area >= 21213:
                    size = "large"
                else:
                    size = "medium"

        else:                                                                                                           #logic for circle
            area = cv2.contourArea(contours[i])
            radius = w / 2                                                                                              #calculating radius of the circle
            if (abs(1 - (float(w) / h)) <= 2 and abs(1 - (area / (math.pi * radius * radius))) <= 0.2):
                shape = "circle"
                if area <= 2286:                                                                                        #logic for size detection
                    size = "small"
                elif area >= 8497:
                    size = "large"
                else:
                    size = "medium"
        cv2.putText(frame, color, (x + w / 3, y + h / 2), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), 1,                #putting text color over image
                    cv2.LINE_AA)
        cv2.putText(frame, shape, (x + w / 3, y + (h / 2) + 15), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), 1,         #putting text shape over image
                    cv2.LINE_AA)

        for j in range(0, len(contours)):                                                                               #logic for similar figures
            
            cnt = contours[j]
            area = cv2.contourArea(cnt)
            approx = cv2.approxPolyDP(contours[j], cv2.arcLength(contours[j], True) * 0.04, True)
            if (abs(cv2.contourArea(contours[j])) < 100 or not (cv2.isContourConvex(approx))):
                continue
            x, y, w, h = cv2.boundingRect(contours[j])
            if (len(approx) == 3):
                shape1 = "triangle"
                if area <= 1585:
                    size1 = "small"
                elif area >= 5663:
                    size1 = "large"
                else:
                    size1 = "medium"
            elif (len(approx) == 4):
                x, y, w, h = cv2.boundingRect(approx)
                ar = w / float(h)
                if ar >= 0.99 and ar <= 1.01:
                    shape1 = "square"
                    if area <= 2913:
                        size1 = "small"
                    elif area >= 10813:
                        size1 = "large"
                    else:
                        size1 = "medium"
                else:
                    shape1 = "rectangle"
                    if area <= 3993:
                        size1 = "small"
                    elif area >= 21213:
                        size1 = "large"
                    else:
                        size1 = "medium"
            else:
                area = cv2.contourArea(contours[j])
                radius = w / 2
                if (abs(1 - (float(w) / h)) <= 2 and abs(1 - (area / (math.pi * radius * radius))) <= 0.2):
                    shape1 = "circle"
                    if area <= 2286:
                        size1 = "small"
                    elif area >= 8497:
                        size1 = "large"
                    else:
                        size1 = "medium"
            if (size1 == size and shape1 == shape):                                                                     #count number of similar figures
                flag = flag + 1

        img = cv2.drawContours(frame, contours, -1, (0, 0, 0), 1)                                                       #drawing contours
        element = []                                                                                                    #creating  a sublist
        element.append(color + "-" + shape + "-" + size + "-" + str(flag))                                              #appending the shapes and colors in the list
        if element not in list:                                                                                         #removing repeated similar images
            list.append(element)                                                                                        #appending the sublist into the list
            writecsv(color, shape, size, flag)                                                                          #calling writecsv function


    canny2, contours, hierarchy = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)              #contour detection for green color
    for i in range(0, len(contours)):                                                                                   #initiating the loop
        color = "green"
        sq = 0
        cnt = contours[i]
        area = cv2.contourArea(cnt)                                                                                     #calculting area of contour
        approx = cv2.approxPolyDP(contours[i], cv2.arcLength(contours[i], True) * 0.04, True)                           #finding of vertices
        if (abs(cv2.contourArea(contours[i])) < 100 or not (cv2.isContourConvex(approx))):
            continue
        x, y, w, h = cv2.boundingRect(contours[i])
        if (len(approx) == 3):                                                                                          #logic for triangle
            shape = "triangle"
            if area <= 1585:                                                                                            #logic for size detection
                size = "small"
            elif area >= 5663:
                size = "large"
            else:
                size = "medium"
        elif (len(approx) == 4):                                                                                        #logic for shape having 4 sides
            x, y, w, h = cv2.boundingRect(approx)
            ar = w / float(h)
            if ar >= 0.99 and ar <= 1.01:                                                                               #logic for square
                shape = "square"
                if area <= 2913:                                                                                        #logic for size detection
                    size = "small"
                elif area >= 10813:
                    size = "large"
                else:
                    size = "medium"
            else:                                                                                                       #logic for rectangle
                shape = "rectangle"
                if area <= 3993:                                                                                        #logic for size detection
                    size = "small"
                elif area >= 21213:
                    size = "large"
                else:
                    size = "medium"
        else:                                                                                                           #logic for circle
            area = cv2.contourArea(contours[i])
            radius = w / 2                                                                                              #calculating radius of the circle
            if (abs(1 - (float(w) / h)) <= 2 and abs(1 - (area / (math.pi * radius * radius))) <= 0.2):
                shape = "circle"
                if area <= 2286:                                                                                        #logic for size detection
                    size = "small"
                elif area >= 8497:
                    size = "large"
                else:
                    size = "medium"
        cv2.putText(frame, color, (x + w / 3, y + h / 2), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), 1, cv2.LINE_AA)   #putting text color over image
        cv2.putText(frame, shape, (x + w / 3, y + (h / 2) + 15), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), 1,         #putting text shape over image
                    cv2.LINE_AA)

        for j in range(0, len(contours)):                                                                               #logic for similar images

            cnt = contours[j]
            area = cv2.contourArea(cnt)
            approx = cv2.approxPolyDP(contours[j], cv2.arcLength(contours[j], True) * 0.04, True)
            if (abs(cv2.contourArea(contours[j])) < 100 or not (cv2.isContourConvex(approx))):
                continue
            x, y, w, h = cv2.boundingRect(contours[j])
            if (len(approx) == 3):
                shape1 = "triangle"
                if area <= 1585:
                    size1 = "small"
                elif area >= 5663:
                    size1 = "large"
                else:
                    size1 = "medium"
            elif (len(approx) == 4):
                x, y, w, h = cv2.boundingRect(approx)
                ar = w / float(h)
                if ar >= 0.99 and ar <= 1.01:
                    shape1 = "square"
                    if area <= 2913:
                        size1 = "small"
                    elif area >= 10813:
                        size1 = "large"
                    else:
                        size1 = "medium"
                else:
                    shape1 = "rectangle"
                    if area <= 3993:
                        size1 = "small"
                    elif area >= 21213:
                        size1 = "large"
                    else:
                        size1 = "medium"
            else:
                area = cv2.contourArea(contours[j])
                radius = w / 2
                if (abs(1 - (float(w) / h)) <= 2 and abs(1 - (area / (math.pi * radius * radius))) <= 0.2):
                    shape1 = "circle"
                    if area <= 2286:
                        size1 = "small"
                    elif area >= 8497:
                        size1 = "large"
                    else:
                        size1 = "medium"
            if (size1 == size and shape1 == shape):                                                                     #logic to calculate number of similar figures
                sq = sq + 1

        img = cv2.drawContours(frame, contours, -1, (0, 0, 0), 1)                                                       #drawing contours
        element = []                                                                                                    #creating  a sublist
        element.append(color + "-" + shape + "-" + size + "-" + str(sq))                                                #appending the shapes and colors in the list
        if element not in list:                                                                                         #removinf repeated similar images
            list.append(element)                                                                                        #appending the sublist to the list
            writecsv(color, shape, size, sq)                                                                            #calling writecsv function


    canny2, contours, hierarchy = cv2.findContours(mask_orange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)             #contour detection for orange color
    for i in range(0, len(contours)):                                                                                   #initiating  the loop
        color = "orange"
        sq = 0
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(contours[i], cv2.arcLength(contours[i], True) * 0.04, True)                           #finding the vertices
        if (abs(cv2.contourArea(contours[i])) < 100 or not (cv2.isContourConvex(approx))):
            continue
        x, y, w, h = cv2.boundingRect(contours[i])
        if (len(approx) == 3):                                                                                          #logic for triangle
            shape = "triangle"
            if area <= 1585:                                                                                            #logic for size detection
                size = "small"
            elif area >= 5663:
                size = "large"
            else:
                size = "medium"
                
        elif (len(approx) == 4):                                                                                        #logic for shape having 4 sides
            x, y, w, h = cv2.boundingRect(approx)
            ar = w / float(h)
            if ar >= 0.99 and ar <= 1.01:                                                                               #logic for square
                shape = "square"
                if area <= 2913:                                                                                        #logic for size detection
                    size = "small"
                elif area >= 10813:
                    size = "large"
                else:
                    size = "medium"
            else:                                                                                                       #logic for rectangle
                shape = "rectangle"
                if area <= 3993:                                                                                        #logic for size detection
                    size = "small"
                elif area >= 21213:
                    size = "large"
                else:
                    size = "medium"
        else:                                                                                                           #logic for circle
            area = cv2.contourArea(contours[i])
            radius = w / 2                                                                                              #calculating radius of the circle
            if (abs(1 - (float(w) / h)) <= 2 and abs(1 - (area / (math.pi * radius * radius))) <= 0.2):
                shape = "circle"
                if area <= 2286:                                                                                        #logic for size detection
                    size = "small"
                elif area >= 8497:
                    size = "large"
                else:
                    size = "medium"
        cv2.putText(frame, color, (x + w / 3, y + h / 2), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), 1, cv2.LINE_AA)   #putting text color over image
        cv2.putText(frame, shape, (x + w / 3, y + (h / 2) + 15), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), 1,         #putting text shape over image
                    cv2.LINE_AA)

        for j in range(0, len(contours)):                                                                               #logic for similar figures

            cnt = contours[j]
            area = cv2.contourArea(cnt)
            approx = cv2.approxPolyDP(contours[j], cv2.arcLength(contours[j], True) * 0.04, True)
            if (abs(cv2.contourArea(contours[j])) < 100 or not (cv2.isContourConvex(approx))):
                continue
            x, y, w, h = cv2.boundingRect(contours[j])
            if (len(approx) == 3):
                shape1 = "triangle"
                if area <= 1585:
                    size1 = "small"
                elif area >= 5663:
                    size1 = "large"
                else:
                    size1 = "medium"
            elif (len(approx) == 4):
                x, y, w, h = cv2.boundingRect(approx)
                ar = w / float(h)
                if ar >= 0.99 and ar <= 1.01:
                    shape1 = "square"
                    if area <= 2913:
                        size1 = "small"
                    elif area >= 10813:
                        size1 = "large"
                    else:
                        size1 = "medium"
                else:
                    shape1 = "rectangle"
                    if area <= 3993:
                        size1 = "small"
                    elif area >= 21213:
                        size1 = "large"
                    else:
                        size1 = "medium"
            else:
                area = cv2.contourArea(contours[j])
                radius = w / 2
                if (abs(1 - (float(w) / h)) <= 2 and abs(1 - (area / (math.pi * radius * radius))) <= 0.2):
                    shape1 = "circle"
                    if area <= 2286:
                        size1 = "small"
                    elif area >= 8497:
                        size1 = "large"
                    else:
                        size1 = "medium"
            if (size1 == size and shape1 == shape):                                                                     #logic to count number of similar figures
                sq = sq + 1

        img = cv2.drawContours(frame, contours, -1, (0, 0, 0), 1)                                                       #drawing contours
        element = []                                                                                                    #creating  a sublist
        element.append(color + "-" + shape + "-" + size + "-" + str(sq))                                                #appending the shapes and colors in the list
        if element not in list:                                                                                         #removing repeated similar images
            list.append(element)                                                                                        #appending
            writecsv(color, shape, size, sq)                                                                            #calling writecsv function
        
        
    canny2, contours, hierarchy = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)             #contour detection for green color
    for i in range(0, len(contours)):                                                                                   #initiating the loop
        count1 = 0
        color = "yellow"
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(contours[i], cv2.arcLength(contours[i], True) * 0.04, True)
        if (abs(cv2.contourArea(contours[i])) < 100 or not (cv2.isContourConvex(approx))):
            continue
        x, y, w, h = cv2.boundingRect(contours[i])
        if (len(approx) == 3):                                                                                          #logic for triangle
            shape = "triangle"
            if area <= 1585:                                                                                            #logic for size detection
                size = "small"
            elif area >= 5663:
                size = "large"
            else:
                size = "medium"

        elif (len(approx) >= 4 and len(approx) <= 6):                                                                   #logic for shapes having edges 4 to 6 sides
            ar = w / float(h)
            if ar >= 0.99 and ar <= 1.01:                                                                               #logic for square
                shape = "square"
                if area <= 2913:                                                                                        #logic for size detection
                    size = "small"
                elif area >= 10813:
                    size = "large"
                else:
                    size = "medium"
            else:                                                                                                       #logic for rectangle
                shape = "rectangle"
                if area <= 3993:                                                                                        #logic for size detection
                    size = "small"
                elif area >= 21213:
                    size = "large"
                else:
                    size = "medium"

        else:
            area = cv2.contourArea(contours[i])                                                                         #logic for circle
            radius = w / 2                                                                                              #calculating radius of the circle
            if (abs(1 - (float(w) / h)) <= 2 and abs(1 - (area / (math.pi * radius * radius))) <= 0.2):
                shape = "circle"
                if area <= 2286:
                    size = "small"
                elif area >= 8497:
                    size = "large"
                else:
                    size = "medium"
        cv2.putText(frame, color, (x + w / 3, y + h / 2), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), 1,                #putting text color over image
                    cv2.LINE_AA)
        cv2.putText(frame, shape, (x + w / 3, y + (h / 2) + 15), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), 1,         #putting text shape over image
                    cv2.LINE_AA)

        for j in range(0, len(contours)):                                                                               #logic for similar figures

            cnt = contours[j]
            area = cv2.contourArea(cnt)
            approx = cv2.approxPolyDP(contours[j], cv2.arcLength(contours[j], True) * 0.04, True)
            if (abs(cv2.contourArea(contours[j])) < 100 or not (cv2.isContourConvex(approx))):
                continue
            x, y, w, h = cv2.boundingRect(contours[j])
            if (len(approx) == 3):
                shape1 = "triangle"
                if area <= 1585:
                    size1 = "small"
                elif area >= 5663:
                    size1 = "large"
                else:
                    size1 = "medium"
            elif (len(approx) == 4):
                x, y, w, h = cv2.boundingRect(approx)
                ar = w / float(h)
                if ar >= 0.99 and ar <= 1.01:
                    shape1 = "square"
                    if area <= 2913:
                        size1 = "small"
                    elif area >= 10813:
                        size1 = "large"
                    else:
                        size1 = "medium"
                else:
                    shape1 = "rectangle"
                    if area <= 3993:
                        size1 = "small"
                    elif area >= 21213:
                        size1 = "large"
                    else:
                        size1 = "medium"
            else:
                area = cv2.contourArea(contours[j])
                radius = w / 2
                if (abs(1 - (float(w) / h)) <= 2 and abs(1 - (area / (math.pi * radius * radius))) <= 0.2):
                    shape1 = "circle"
                    if area <= 2286:
                        size1 = "small"
                    elif area >= 8497:
                        size1 = "large"
                    else:
                        size1 = "medium"
            if (size1 == size and shape1 == shape):                                                                     #logic to count  number of similar figures
                count1 = count1 + 1

        img = cv2.drawContours(frame, contours, -1, (0, 0, 0), 1)                                                       #drawing contours
        element = []                                                                                                    #creating a sublist
        element.append(color + "-" + shape + "-" + size + "-" + str(count1))                                            #appending the shapes and colors in  the list
        if element not in list:                                                                                         #removing repeated similar images
            list.append(element)                                                                                        #appending the sublist in the list
            writecsv(color, shape, size, count1)                                                                        #calling writecsv function


    cv2.imshow('frame', frame)                                                                                          #showing the output image
    temp = filter(lambda x: x != "t", path)                                                                             #logic to remove  the word "test" fromt the name of the output image
    temp = filter(lambda x: x != "e", temp)
    temp = filter(lambda x: x != "s", temp)
    temp = filter(lambda x: x != "t", temp)
    output_name= "output" +temp                                                                                         #appending "output" to the number of image with extension .png
    cv2.imwrite(output_name, frame)                                                                                     #saving the output image
    cv2.waitKey(0)                                                                                                      #waiting for the user to press any key
    cv2.destroyAllWindows()                                                                                             #closing the opened windows
    return list                                                                                                         #returning the list when main() is called
if __name__ == "__main__":
    mypath = '.'
    #getting all files in the directory
    onlyfiles=[]
    for f in os.listdir(mypath):
        if f.endswith(".png"):
            onlyfiles.append(f)
    for fp in onlyfiles:
        #Open the csv to write in append mode
        filep = open('results1B_943.csv','a')
        #this csv will later be used to save processed data, thus write the file name of the image
        filep.write(fp)
        #close the file so that it can be reopened again later
        filep.close()
        #process the image
        data = main(fp)
        print data
        #open the csv
        filep = open('results1B_943.csv','a')
        #make a newline entry so that the next image data is written on a newline
        filep.write('\n')
        #close the file
        filep.close()
