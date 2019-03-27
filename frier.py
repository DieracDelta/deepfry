from PIL import Image
from tesserocr import PyTessBaseAPI, RIL
import random
import sys





if __name__ == "__main__":
    # TODO make limit dependent on number of letters
    # TODO pass in maim_location as part of argv
    #sys.stderr.write(str(sys.argv))
    maim_location = "/tmp/maim_screenie.png"
    maim_location_2 = "/tmp/maim_screenie2.png"
    b_location = sys.argv[8]
    limit = 0.80
    total_command = "convert -page " + str(sys.argv[1]) + "x" + str(sys.argv[2]) + "+0+0 " + maim_location + " "
    image = Image.open(maim_location)
    with PyTessBaseAPI() as api:
        api.SetImage(image)
        boxes = api.GetComponentImages(RIL.SYMBOL, True)
        for _, (__, box, _, _) in enumerate(boxes):
            if random.random() > limit: 
                total_command += " -page " + str(sys.argv[3]) + "x" + str(sys.argv[4]) + "+" + str(box['x']) + "+" + str(box['y'] - 6) + " " + b_location + " "
    print(total_command + " -background dodgerblue -layers flatten " + maim_location_2 + "  ")
