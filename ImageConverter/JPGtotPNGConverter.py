import sys
import os
from PIL import Image
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--imgfold', type=str, required=True)
    parser.add_argument('--outfold', type=str, required=True)
    args = parser.parse_args()
    
    image_folder = args.imgfold
    output_folder = args.outfold
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(image_folder):
        img = Image.open(f"{image_folder}{file}")
        clean_filename = clean_name_from_extension(file)
        img.save(f"{output_folder}\{clean_filename}.png",'png')
        print(file, " is done being converted!")
        
def clean_name_from_extension(filename):
    return filename.replace('.jpg','')
if __name__ == '__main__':
    main()