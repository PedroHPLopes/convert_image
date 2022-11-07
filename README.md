# Convert Images: Convert all images in a given folder to the desired extension
By Pedro Lopes 

### Introduction 
This repository contains a script to automatically convert all images in a folder to the wanted extension. The script also performs other treatments, such as **rescaling**, **rotation** and **grayscale conversion**. 
This project was inspired by the first assignement of the [Course Automating Real-World Tasks with Python](https://www.coursera.org/learn/automating-real-world-tasks-python). This script was made to be generic and have many more use cases. The `images` directory is directly extracted from the course.

### Requirements
Requirements can be found in the `environment.yml` file.

### Usage
To use this script, one must run on a terminal:
```console
python convert_images.py <folder_path>
```
Default behaviour will convert all files in `folder_path` to the **png** extension, and saved them at `treated_images`. There are several flags available to the user:
    * `-t`, `--type` desired_extension - Defines the desired extension for the output images. defaults to `png`
    * `-o` `--output` outfolder - Defines the output folder where converted images will be saved. Defaults to `treated_images`
    * `-s` `--rescale` width height - Defines the width and height that the new image should be rescaled to. Bothe values should be positive integers. Defaults to `None`
    * `-r` `--rotate` degrees - Defines the degrees in which the image will be rotated. This value should be an integer. Defaults to `None`.
    * `-g` `--grayscale` - Flag to be passed if the user desires to save the image as grayscale.
    * `-v` `--verbose` - Flag to be passed to activate verbose. By default, the script will print only messages for images that were not opened by any reason. If activated, it will print a message containing all the treatments made for the image and where it was saved.
    * `-l` `--log` - Flag to be passed to if the user wishes to save treatment information on a file, `log_file.txt`. The information is exactly the same as the one printed if verbose is activated. 

### Examples 
The example given here is the same as used in Coursera's assignment. The images in `images` need to be converted to the png image format, rotated by -90 degrees and rescaled to (128,128). To achieve this using this script, une should run the command: 
```console
python convert_image.py images -s 128 128 -r -90
```
If the verbose flag is activated, informations will be printed as such:
```console
ic_near_me_black_48dp:Rotated by -90 degrees. Rescaled from (192, 192) to (128, 128). Saved at treated_images\ic_near_me_black_48dp.png.
```