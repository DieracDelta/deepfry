#! /usr/bin/env python
from PIL import Image
from tesserocr import PyTessBaseAPI, RIL
import random
import functools
import subprocess
import os


if __name__ == "__main__":
    b_location = os.environ.get("B_LOCATION")
    if b_location is None or b_location == "":
        print("error, B_LOCATION was unset")
        exit(0)

    maim_location = "/tmp/maim_screenie.png"
    maim_location_2 = "/tmp/maim_screenie2.png"
    maim_location_3 = "/tmp/maim_screenie3.png"

    try:
        subprocess.check_call(["rm", maim_location])
        subprocess.check_call(["rm", maim_location_2])
        subprocess.check_call(["rm", maim_location_3])
    except Exception:
        pass

    if os.getenv("DISPLAY_FRONTEND") == "X11":
        subprocess.check_call(["maim", "-s", maim_location])
    else:
        slurp = subprocess.check_output("slurp")
        subprocess.check_call(
            ["grim", "-g", slurp[:-1], maim_location]
        )

    # subprocess.check_call(
    # ["cp", "\"" + maim_location + "\"", "\"" + maim_location_3 + "\""]
    # )

    dims_screenshot = subprocess.check_output(
        ["identify", "-format", "\"%w %h \"", maim_location]
    )
    dims_screenshot = dims_screenshot.decode("utf-8").split(" ")
    dims_b = subprocess.check_output(
        ["identify", "-format", "\" %w %h \" ", b_location]
    )
    # subprocess.check_call("touch", main_location_2)
    # print("dim_b" + str(dims_b))
    # print("dim_b" + str(dims_screenshot))

    limit = 0.40
    total_command = ["convert", "-page", dims_screenshot[0]
                     [1:]+"x"+dims_screenshot[1]+"+0+0", maim_location]
    image = Image.open(maim_location)
    with PyTessBaseAPI() as api:
        api.SetImage(image)
        boxes = api.GetComponentImages(RIL.SYMBOL, True)
        for _, (__, box, _, _) in enumerate(boxes):
            if random.random() > limit:
                total_command += ["-page", dims_screenshot[0][1:] +
                                  "x" + dims_screenshot[1] +
                                  "+" + str(box['x']) + "+"
                                  + str(box['y'] - 6), b_location]
    total_command += ["-background", "dodgerblue",
                      "-layers", "flatten", maim_location_2]
    # print(functools.reduce(lambda a, b: a + " " + b, total_command))
    subprocess.check_call(["touch", maim_location_2])
    subprocess.check_call(["touch", maim_location_3])
    image.close()
    subprocess.check_call(total_command)
    # TODO change the wl-copy based on X vs wayland
    subprocess.check_call(
        ["bash", "-c", "convert " + maim_location_2 + " -liquid-rescale "
         " 50% " + " -fill " + " orange " + " -tint " + " 100 " +
         " - " + " | " + " convert " + " - " + " -liquid-rescale "
         + " 200% " + " - " + " | " + " convert " + " - " + " -modulate " +
         " 50,200 " + " - " + " | " + " convert " + " - " + " -emboss " +
         " -x1.1 " + " - " + " | " + " wl-copy "]
    )
