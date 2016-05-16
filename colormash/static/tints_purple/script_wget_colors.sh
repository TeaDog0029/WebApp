#!/bin/bash
while read TINT; do
   wget http://www.beautycolorcode.com/$TINT.png
done <tints_purple.txt