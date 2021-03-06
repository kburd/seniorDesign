from PIL import Image
from email.mime.multipart import MIMEMultipart
import smtplib
import os
import sys
import click
from pathlib import Path

#Cmd Line:  python <location of this file> <name of tub> <color> <fill or tint>
#Ex:        python C:\Users\kaleb\PycharmProjects\SeniorDesign\filter.py tub_1_18-03-04 r f




def filterImage(image,color,tint):

    sideLength = 20
    yPosition = 5

    width, height = image.size

    pix = image.load()

    for i in range((width // 2) - (sideLength // 2), (width // 2) + (sideLength // 2)):
        for j in range(yPosition, sideLength + yPosition):

            red = pix[i, j][0]
            green = pix[i, j][1]
            blue = pix[i, j][2]

            if color == "r":
                red = 255

                if tint == "f":
                    green = 0
                    blue = 0

            elif color == "g":
                green = 255

                if tint == "f":
                    red = 0
                    blue = 0

            elif color == "b":
                if tint == "f":
                    green = 0
                    red = 0

            pix[i, j] = (red, green, blue)

    return image


def filterTub(tubName,color, tint):

    directory = "C:\\Users\\kaleb\\d2\\data"

    absoluteTubName = directory + "\\" + tubName + "\\" + tubName
    allFiles = os.listdir(absoluteTubName)

    newTubName = tubName + "Filtered"
    newAbsoluteTubName = directory + "\\" + newTubName + "\\" + newTubName

    if not os.path.exists(newAbsoluteTubName):
        os.makedirs(newAbsoluteTubName)

    for file in allFiles:

        extension = file.split(".")[1]

        if extension == "jpg":

            im = Image.open(absoluteTubName + "\\" + file)

            im = filterImage(im,color,tint)
            new_image_path = Path(newTubPath / file.name)
            im.save(new_image_path.absolute())


def emailIP():


    emailfrom = "navigatorSeniorDesign@gmail.com"
    password = "navigator18"


    emailto = "navigatorSeniorDesign@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = emailfrom
    msg['To'] = emailto
    msg['Subject'] = 'IP HERE'

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(emailfrom, password)
    server.sendmail(emailfrom, emailto, msg.as_string())
    server.quit()


if __name__ == "__main__":
#
#     # args = sys.argv
#     # tubName = args[1]
#     # color = args[2]
#     # tint = args[3]
    filterTub()
#     #filterTub(tubName, color, tint)
