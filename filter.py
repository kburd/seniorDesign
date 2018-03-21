from PIL import Image
import os
import sys
import click
from pathlib import Path

#Cmd Line:  python <location of this file> <name of tub> <color> <fill or tint>
#Ex:        python C:\Users\kaleb\PycharmProjects\SeniorDesign\filter.py tub_1_18-03-04 r f



directory = "C:\\Users\\kaleb\\d2\\data"



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

@click.command()
@click.argument('tubname', type=click.Path(exists=True, dir_okay=True, file_okay=False, readable=True))
@click.argument('dst', type=click.Path(exists=True, dir_okay=True, file_okay=False, writable=True))
@click.argument('color', type=click.Choice(['r','g','b']))
@click.argument('tint', type=click.Choice(['t','f']))
def filterTub(tubname, dst, color, tint):
    #The location of the tub images
    tubPath = Path(tubname)
    #The location where they will be saved
    destination = Path(dst)
    newTubName = tubPath.name + "_filtered"
    newTubPath = destination / newTubName
    newTubPath.mkdir(exist_ok=True, parents=True)
    
    with click.progressbar(tubPath.glob('*.jpg')) as tub_images:
        #Iterate through all of the jpgs
        for file in tub_images:
            extension = file.name.split(".")[1]
            im = Image.open(file.absolute())
            im = filterImage(im,color,tint)
            new_image_path = Path(newTubPath / file.name)
            im.save(new_image_path.absolute())


if __name__ == "__main__":
#
#     # args = sys.argv
#     # tubName = args[1]
#     # color = args[2]
#     # tint = args[3]
    filterTub()
#     #filterTub(tubName, color, tint)
