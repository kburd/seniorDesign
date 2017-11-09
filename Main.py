import cv2
import numpy as np
import serial
import Thought as th

def alignmentAdjustment(thought):

    # Take in image and calculate hough lines
    gray = cv2.cvtColor(thought.image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 100, apertureSize=3)  # 75,100
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

    height = len(thought.image)
    width = len(thought.image[0])

    # print(type(lines))
    tempLines = []

    if (lines is None or lines.all() == None):
        return "---------------"

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

            #removes all the horizontal ones ie under 30 degrees
            if abs(90-180*theta/np.pi) > 30:
                tempLines.append(line)
                if thought.display:
                    cv2.line(thought.image,(x1,y1),(x2,y2),(0,0,255),2)

                    # Redefines appropriate values to lines
        lines = tempLines

        xAvg = 0
        yAvg = 0
        count = 0

    # locate all intersections and take average of coordinates
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

        for j in range(i, len(lines)):

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

            # some funky alegbra I found online
            d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if d != 0:
                xtemp = ((x3 - x4) * (x1 * y2 - y1 * x2) - (x1 - x2) * (x3 * y4 - y3 * x4)) / d
                ytemp = ((y3 - y4) * (x1 * y2 - y1 * x2) - (y1 - y2) * (x3 * y4 - y3 * x4)) / d

                # ignore if outside of image
                if xtemp >= 0 and xtemp <= width and ytemp >= 0 and ytemp <= height:
                    xAvg += xtemp
                    yAvg += ytemp
                    count += 1

    # Calculate averages
    if count == 0:
        xi = int(width / 2)
        yi = int(height / 2)
    else:
        xAvg /= count
        yAvg /= count
        xi = int(xAvg)
        yi = int(yAvg)

    if thought.display:
        # draws box around vanishing point
        threshold = 15
        for i in range(2 * threshold):
            cv2.line(thought.image, (xi - threshold, yi - threshold + i), (xi + threshold, yi - threshold + i), (255, 0, 0), 2)

        # draws lines from corners to vanishing point
        cv2.line(thought.image, (xi, yi), (0, height), (0, 255, 0), 2)
        cv2.line(thought.image, (xi, yi), (width, height), (0, 255, 0), 2)

        # Displays image
        cv2.imshow("dat", thought.image)

    # Left/Right/Straight Logic
    if width / 2 - xi < -width / 5:
        # turn right
        print("<")
        return b'q'

    elif width / 2 - xi > width / 5:
        # turn left
        print(">")
        return b'e'

    else:
        # go straight
        print("^")
        return b'w'

def main():

    i = 0;
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    # ser = serial.Serial('/dev/cu.usbmodem1411', 9600)

    showImages = True
    thought = th.Thought(None, showImages)

    while 1:

        ret, thought.image = cap.read()

        if (i % 7 == 0):
            i = 0
            direction = alignmentAdjustment(thought)

            # ser.write(direction)
            # ser.write(b'v')

        #Quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        i+=1

main()