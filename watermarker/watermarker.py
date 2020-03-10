#!/usr/bin/env python

"""Watermarker is a simple script to resize, crop, and watermark images uniformly.
The formatted images are saved as a new file into a designated folder to preserve
the original images.

Make sure to replace the watermark.png image with a watermark image of your choice.
If you use 'watermark.png' as the file name, no code will need changing.

Default resize is 2000 x 2000 px.  Change the new_size variable if a different size
is needed."""

import os
from tkinter.filedialog import askdirectory

from PIL import Image

# -----  Variables you may need to change  -----

# Open and assign watermark image file to variable "watermark"
# !!!  REPLACE THIS FILE WITH YOUR WATERMARK IMAGE  !!!
watermark = Image.open("resources/watermark.png")

# Desired pixel width and height of final image
# !!!  REPLACE THESE DIMENSIONS WITH YOUR PREFERRED IMAGE SIZE !!!
# Format: (width, height) in integer count of pixels
new_size = (2000, 2000)
new_width, new_height = new_size

# -----

# TODO: Improve the user interface with more informative user prompts
# TODO: This doesn't show the files within the directory, look for better implementation
# Ask user to select file folder from which to open images
open_folder = askdirectory(
    title='Select the folder from which to import images')
# Ask user to select file folder in which to save new images
new_folder = askdirectory(
    title='Select the save folder for completed images')

# Create a loop to iterate through each image file
for img_file in os.listdir(open_folder):
    # Set complete filepath as a variable
    img_filepath = open_folder + '/' + img_file

    # Verify file is a valid image file and open
    try:
        orig_img = Image.open(img_filepath)
    except IOError:
        continue

    # Assign image filename - file extension to string variable "orig_img_name"
    orig_img_name = img_file.rsplit('.', 1)[0]
    # Create image copy and assign to variable "new_img"
    new_img = orig_img.copy()
    # Create variables for width and height of new_img
    orig_width, orig_height = new_img.size
    # Create Boolean "too_small" set to False
    too_small = False
    # If new_img's height or width is smaller than desired size, set too_small to True
    if new_img.size[0] < new_size[0] or new_img.size[1] < new_size[1]:
        too_small = True

    # Resize based on smallest dimension
    resize_width = 0
    resize_height = 0
    if orig_width < orig_height:
        resize_width = new_width
        resize_height = int(orig_height * (new_width / orig_width))
    else:
        resize_width = int(orig_width * (new_height / orig_height))
        resize_height = new_height

    # Resize new_img to desired size
    new_img = new_img.resize((resize_width, resize_height), Image.ANTIALIAS)
    # Get coordinates for centering crop
    left = int((resize_width - new_width) / 2)
    top = int((resize_height - new_height) / 2)
    right = int((resize_width + new_width) / 2)
    bottom = int((resize_height + new_height) / 2)
    # Crop image, centered
    new_img = new_img.crop((left, top, right, bottom))

    # TODO: Give user the option of selecting watermark location
    # Overlay watermark onto bottom left corner of image as transparent by using
    # itself as the mask, thus only pasting opaque pixels
    new_img.paste(watermark,
                  (new_width - watermark.size[0],
                   new_height - watermark.size[1]),
                  watermark)

    # If too_small, shrink back to original resolution using smallest dimension
    if too_small:
        if orig_width < orig_height:
            shrink_width = orig_width
            shrink_height = int(orig_height * (new_width / orig_width))
        else:
            shrink_width = int(orig_width * (new_height / orig_height))
            shrink_height = orig_height

        new_img.thumbnail((shrink_width, shrink_height))

    # Save result as orig_img_name + "_marked.png" in new_folder
    new_img.save("{}/{}_marked.png".format(new_folder, orig_img_name))

    # TODO: Is "processed" the best name?  Maybe prompt user to name folder instead
    # If "processed" folder does not exist, create
    if not os.path.isdir(open_folder + '/processed'):
        os.mkdir(open_folder + '/processed')

    # Move orig_img to “processed” folder
    os.replace(img_filepath, "{}/processed/{}".format(open_folder, img_file))

    # TODO: Add "finished" message
