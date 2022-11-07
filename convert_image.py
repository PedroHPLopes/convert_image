import os
from re import I
from PIL import Image, ImageOps
import argparse
from tqdm import tqdm 

IMAGE_FORMATS = ["png", "jpeg", "tiff"]

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def main(args):

    folder_path = args.folder
    out_folder = args.out
    im_type = args.type
    files_list = os.listdir(folder_path)

    mkdir(out_folder)

    log_list = []

    for file_name in tqdm(files_list):
        file = os.path.join(folder_path, file_name)

        info = "{}:".format(file_name)
        
        # Check if is a directory
        if os.path.isdir(file):
            info += "Is a directory"
            tqdm.write(info)
            if args.log:
                log_list.append(info)

            continue
        
        # Check if it's a valid image type
        try: 
            src_img=Image.open(file)
        except:
            info += "Not a valid image type."
            tqdm.write(info)
            if args.log:
                log_list.append(info)
            continue

        img = src_img.copy()
        
        # Image must be converted to RGB if the desired extension is jpeg
        if im_type == "jpeg":
            img = img.convert('RGB')
        # Rotate Image
        if args.rotate is not None:
            img = img.rotate(args.rotate)
            info += "Rotated by {} degrees. ".format(args.rotate) 
            
        # Rescale Image
        if args.rescale is not None:
            new_scale = tuple(args.rescale)
            img = img.resize(new_scale)
            info += "Rescaled from {} to {}. ".format(src_img.size, new_scale) 
        
        # Convert to grayscale
        if args.grayscale:
            img = ImageOps.grayscale(img)
            info += "Converted to Grayscale. "

        # Save image

        out_name = os.path.join(out_folder, file_name+"."+im_type)
        img.save(out_name, im_type)
        info += "Saved at {}.".format(out_name)
        
        # If verbose is activated - print to screen
        if args.verbose:
            tqdm.write(info)

        # Append info to log list
        if args.log:
            log_list.append(info)

    if args.log:
        with open("log_file.txt", "w") as f:
            for log_line in log_list:
                f.write(log_line + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog = 'Convert Image',
                    description = 'This program converts type of all images in a given folder, and also performs other operations such as rescale and rotation',
                    epilog = 'Text at the bottom of help')
                
    parser.add_argument("folder")
    parser.add_argument("-t", "--type",dest="type", type = str,
                        help="Desired image extension",
                        choices = IMAGE_FORMATS, default="png")
    parser.add_argument("-o", "--out", dest = "out", type = str,
                        help="Output folder", default="treated_images")       
    parser.add_argument("-s", "--rescale",dest="rescale", type = int,
                        help="Desired image dimensions", nargs=2, default=None) 
    parser.add_argument("-r", "--rotate",dest="rotate", type = int,
                        help="Desired rotation in degrees", default = None)

    parser.add_argument("-g", "--grayscale",dest="grayscale",
                        help="Flag to activate to save the image in grayscale",
                        action="store_true")

    parser.add_argument("-v", "--verbose",dest='verbose', action = "store_true", help="Flag to activate verbose")

    parser.add_argument("-l", "--log",dest='log', action = "store_true", help="Flag to activate to save a log file for each conveted file")

    main(parser.parse_args())