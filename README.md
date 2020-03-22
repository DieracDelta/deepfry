# What is this? 
A script that deepfries whatever you select, and copies the deepfried image to your clipboard
# Dependencies 
- slurp
- grim
- wayland
- imagemagick configured with the `--with-lqr=yes` before compilation
- liblqr
- python 3.7
- tesseract ocr to install this: `pip3 install --user tesserocr`
# Install and usage
To run: `python3.7 frier.py`. You need to first set `$B_LOCATION` to the location of `bsmol.png`. Sample invocation: `B_LOCATION=$(pwd)/bsmol.png python3.7 frier.py`. Note that a nix package for this lives [here](https://github.com/DieracDelta/nix_home_manager_configs/tree/master/pkgs/deepfry). In this case, you need not set the png location --just invoke with `deepfry`.
