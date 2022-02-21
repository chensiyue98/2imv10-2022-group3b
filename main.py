import os
import rawpy
import numpy as np
import argparse

parser = argparse.ArgumentParser(description="Processes a set of images using the HDR+ pipeline.")

parser.add_argument("input", help="Path to a directory of images to process.")
parser.add_argument("output", help="Path where output should be saved to.")
parser.add_argument("-s", "--stages", help="Should be X:Y. Process from stage X to Y.")
parser.add_argument("-v", "--verbosity", action="store_true", help="Print detailed information while processing.")

args = parser.parse_args()

def main():
    print(f"Input: {args.input}")
    print(f"Output: {args.output}")

# Loads a raw image
def load_image(path):
    with rawpy.imread(path) as raw:
        image = raw.raw_image.copy() # returns a 2D ndarray array, grey scale
        image_rgb = raw.postprocess() # returns a 3D ndarray array, rgb channels
        return image

# Loads a burst of images from a folder
def load_burst(path):
    # Get the file list in the path
    file_list = os.listdir(path)
    # Remove the .DS_Store file on MacOS
    for item in file_list:
        if item.startswith('.') and os.path.isfile(os.path.join(path, item)):
            file_list.remove(item)
    # Load the images
    images = []
    for item in file_list:
        images.append(load_image(f'test_data/{item}'))
    return images

if __name__ == '__main__':
    main()

