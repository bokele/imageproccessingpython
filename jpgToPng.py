import sys
import os
from PIL import Image



#get the first and the second argument from prompt line
image_folder = sys.argv[0]
output_image_folder = sys.argv[1]

#check the is new/ exists, if not create it
if not os.path.exists(output_image_folder):
    os.makedirs(output_image_folder)

#loop through the image folder

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f"{output_image_folder}{clean_name}.png", "png")


# convert the images to png


# save the to the new folder