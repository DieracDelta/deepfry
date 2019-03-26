#!/bin/bash
MAIM_LOCATION="/tmp/maim_screenie.png"
MAIM_LOCATION_2="/tmp/maim_screenie2.png"
# change this line to wherever your cloned the script
ROOT="/home/dieraca/summer_18_projs/deepfrier"
B_LOCATION="$ROOT/bsmol.png"
maim -s $MAIM_LOCATION
dims_screenie=$(identify -format " %w %h " $MAIM_LOCATION)
dims_b=$(identify -format " %w %h " $B_LOCATION)
deepfry=$(python3.6 $ROOT/frier.py $dims_screenie $dims_screenie $dims_b $MAIM_LOCATION $B_LOCATION)
touch $MAIM_LOCATION_2
$($deepfry)
convert $MAIM_LOCATION_2 -liquid-rescale 50% -fill orange -tint 100 - | convert - -liquid-rescale 200% - | convert - -modulate 50,200 - | convert - -emboss 0x1.1 - | xclip -selection clipboard -t image/png
rm $MAIM_LOCATION
rm $MAIM_LOCATION_2
