# What is this? 
A script that deepfries whatever you select, and copies the deepfried image to your clipboard
# Dependencies 
- slurp, grim, and wayland OR X11 and maim
- imagemagick configured with the `--with-lqr=yes` before compilation
- liblqr
- python 3.7+
- `tesseract ocr`. to install this: `pip3 install --user tesserocr`. Note that this requires, on arch, `leptonica` and `tesseract` libraries; so `yay -S leptonica tesseract`. On debian, this requires: `libtesseract-dev` and (maybe)`tesseract-ocr`. Note that if you experience a segfault with this error: `!strcmp(locale, "C"):Error:Assert failed:in file baseapi.cpp, line 209`, then set your environment variable before you run the script: `export LC_ALL=C`.
# Install and usage
To run: `python3.7 frier.py`. You need to first set `$B_LOCATION` to the location of `bsmol.png`. Sample invocation: `B_LOCATION=$(pwd)/bsmol.png python3.7 frier.py`. Note that a nix package for this lives [here](https://github.com/DieracDelta/nix_home_manager_configs/tree/master/pkgs/deepfry). In this case, you need not set the png location --just invoke with `deepfry`.

To invoke on X11, you'll also need to set the `DISPLAY_FRONTEND` variable to `X11`. Sample invocation:
`DISPLAY_FRONTEND=X11 B_LOCATION=$(pwd)/bsmol.png python3.7 frier.py`
