from PIL import Image
from click import command, argument, Choice
from click import Path as clickPath
from pathlib import Path
from shutil import copy
from tqdm import tqdm

#Try --help for help



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

@command()
@argument('tubname', type=clickPath(exists=True, dir_okay=True, file_okay=False, readable=True))
@argument('dst', type=clickPath(exists=True, dir_okay=True, file_okay=False, writable=True))
@argument('color', type=Choice(['r','g','b']))
@argument('tint', type=Choice(['t','f']))
def filterTub(tubname, dst, color, tint):
    #The location of the tub images
    tubPath = Path(tubname)
    #The location where they will be saved
    destination = Path(dst)
    newTubName = tubPath.name + "_filtered"
    newTubPath = destination / newTubName
    newTubPath.mkdir(exist_ok=True, parents=True)

    #Copy all the json records
    print("Copying records")
    for record in tqdm(tubPath.glob('*.json')):
        toFile = newTubPath / record.name
        copy(str(record), str(toFile))

    print("Copying images")
    #Iterate through all of the jpgs
    for file in tqdm(tubPath.glob('*.jpg')):
        extension = file.name.split(".")[1]
        im = Image.open(file.absolute())
        im = filterImage(im,color,tint)
        new_image_path = Path(newTubPath / file.name)
        im.save(new_image_path.absolute())


if __name__ == "__main__":
    filterTub()
