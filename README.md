# Watermarker

This quick utility resizes, crops, and watermarks images in a folder, saving the watermarked image as a new file in a selected folder.  

* The watermark is applied to the bottom right corner of the image.  
* Watermarks are applied with their original transparency settings.  
* If an image is smaller than the desired resize dimensions, the image will be upsized, processed, and then shrunk back down to its original resolution.
* The original image files are preserved as-is and moved to a "processed" sub-folder within the folder where the original images reside.

## Setup

You will need an image file for your watermark.  Ensure it is the correct size and transparency.  Save your watermark file as "watermark.png" in the resources folder.

Change the new_size dimensions at the top of the watermarker.py file to your desired width and height.  The default is 2000 x 2000 - this is the recommended size for Etsy listing images, and square proportions for posting to social media.  

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
