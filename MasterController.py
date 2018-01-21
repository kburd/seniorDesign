import cv2
import numpy as np

def alignmentAdjustment(img):

    #Take in image and calculate hough lines
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,100,apertureSize = 3) #75,100
    lines = cv2.HoughLines(edges,1,np.pi/180,200)

    height = len(img)
    width = len(img[0])


    # print(type(lines))
    tempLines = []

    if(lines is None or lines.all() == None):
        return "---------------"

    tAvg = 0
    for line in lines:
        for rho,theta in line:

            #calculates start and stop points
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            # cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
            #removes all the horizontal ones ie under 30 degrees
            if abs(90-180*theta/np.pi) > 30:
                cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
                tempLines.append(line)
            tAvg += theta       # add all angles to find average

    tAvg /= len(lines)          # find average angle for direction
    # print("tAvg = ", tAvg)


    #Redefines appropriate values to lines
    lines = tempLines

    xAvg = 0
    yAvg = 0
    count = 0

    #locate all intersections and take average of coordinates
    for i in range(len(lines)):

        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)

        for j in range(i,len(lines)):

            rho = lines[j][0][0]
            theta = lines[j][0][1]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x3 = int(x0 + 1000 * (-b))
            y3 = int(y0 + 1000 * a)
            x4 = int(x0 - 1000 * (-b))
            y4 = int(y0 - 1000 * a)

            #some funky alegbra I found online
            d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if d != 0:
                xtemp = ((x3 - x4) * (x1 * y2 - y1 * x2) - (x1 - x2) * (x3 * y4 - y3 * x4)) / d
                ytemp = ((y3 - y4) * (x1 * y2 - y1 * x2) - (y1 - y2) * (x3 * y4 - y3 * x4)) / d

                #ignore if outside of image
                if xtemp >= 0 and xtemp <= width and ytemp >= 0 and ytemp <= height:

                    xAvg += xtemp
                    yAvg += ytemp
                    count += 1

    #Calculate averages
    if count == 0:
        xi = int(width/2)
        yi = int(height/2)
    else:
        xAvg /= count
        yAvg /= count
        xi = int(xAvg)
        yi = int(yAvg)

    #draws box around vanishing point
    threshold = 15
    for i in range(2*threshold):
        cv2.line(img,(xi-threshold,yi-threshold+i),(xi+threshold,yi-threshold+i),(255,0,0),2)

    #draws lines from corners to vanishing point
    cv2.line(img,(xi,yi),(0,height),(0,255,0),2)
    cv2.line(img,(xi,yi),(width,height),(0,255,0),2)

    #Displays image
    # h, w, layers = img.shape
    # resize = cv2.resize(img, (h/2, w/2))
    cv2.imshow("dat", img)


    #Left/Right/Straight Logic
    if width/2 - xi < -width/5:
        #turn right
        print("<")
        return b'q'

    elif width/2 - xi > width/5:
        #turn left
        print(">")
        return b'e'

    else:
        #go straight
        print("^")
        return b'w'

cap = cv2.VideoCapture("http://128.4.208.193:8080/?action=stream?dummy=frame.mjpg")

while True:

    result,img = cap.read()

    if result:
        alignmentAdjustment(img)
        #cv2.imshow("datass", img)
    else:
        print("Failed to Open")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()