# What is this? 
A script that deepfries whatever you select, and copies the deepfried image to your clipboard
# Dependencies 
- slurp
- grim
- wayland
- imagemagick
- python 3.7
- tesseract ocr to install this: `pip3 install --user tesserocr`
# Install and usage
To run: `bash main.sh`. You need to first set `$B_LOCATION` and `$FRIER_LOCATION` to the paths to `bsmol.png` and `frier.py`, respectively. Sample invocation: `B_LOCATION=$(pwd)/bsmol.png FRIER_LOCATION=$(pwd)/frier.py bash main.sh`. Note that a nix package for this lives [here](https://github.com/DieracDelta/nix_home_manager_configs/tree/master/pkgs/deepfry). You need not set either locations with nix--just invoke with `deepfry`.
