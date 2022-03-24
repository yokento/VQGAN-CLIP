import sys
import os
import cv2
from pathlib import Path as fsPath
from PIL import Image
import subprocess

# load images to bake
root_directory = os.path.abspath(os.getcwd())
# print("root directory: ", root_directory)
# image_directory = os.path.abspath(root_directory + "/batch_input/")
# print("input directory: ", image_directory)
output_directory = os.path.abspath(root_directory + "/batch_output/")

# images = []

# for filename in os.listdir(image_directory):
#     img = cv2.imread(os.path.join(image_directory, filename))
#     if img is not None:
#         images.append(img)

genOutputPath = os.path.abspath(root_directory + "/output.png") #path to generate.py output

for image in range(100):

    # #call anaconda environment shell and call generate.py
    cmd = "python generate.py -ii batch_input/" + str(image) +".png -i 0 -se 1 -s 512 512 "
    subprocess.run(cmd, shell=True)

    my_file_name = str(image) + ".png"
    my_file_name = fsPath(output_directory) / my_file_name
    output = Image.open(genOutputPath).convert("RGB")
    output.save(my_file_name)


print("done")