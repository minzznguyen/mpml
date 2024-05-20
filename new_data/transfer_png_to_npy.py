# make X as in the model project
# aka transfer png to npy file 

import os
import numpy as np
import cv2

# Define the directories containing the images
true_image_dir = '/Users/jamesnguyen/SchoolResources/AI/image_recognition_project/new_data/images/True'
false_image_dir = '/Users/jamesnguyen/SchoolResources/AI/image_recognition_project/new_data/images/False'

# Initialize empty lists to store the image arrays and labels
image_list = []
label_list = []

# Set the desired image size
image_size = (100, 100)  # or any other desired size

# Function to load images from a directory
def load_images_from_directory(directory, label):
    for filename in os.listdir(directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Load the image
            img_path = os.path.join(directory, filename)
            image = cv2.imread(img_path)
            
            # Resize the image to a consistent size
            image = cv2.resize(image, image_size)
            
            # Convert the image to grayscale (optional)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Flatten the image to a 1D array
            image = image.flatten()
            
            # Append the image and label to the lists
            image_list.append(image)
            label_list.append(label)

# Load True images
load_images_from_directory(true_image_dir, 1)

# Load False images
load_images_from_directory(false_image_dir, 0)

# Stack all image arrays into a single NumPy array
image_array = np.array(image_list)
label_array = np.array(label_list)

# Save the arrays to .npy files
np.save('images.npy', image_array)
np.save('labels.npy', label_array)

print(f'Saved {len(image_list)} images to images.npy')
print(f'Saved {len(label_list)} labels to labels.npy')
print(f'The shape of X is: {image_array.shape}')
print(f'The shape of y is: {label_array.shape}')
