import csv
from PIL import Image
import os


def resize_and_store_image(input_path, output_path, new_size):
    """
    Resize an input image and store the resized image.

    - input_path (str): Path to the input image.
    - output_path (str): Path to store the resized image.
    - new_size (int, int): Tuple specifying the new size (width, height) of the image.
    """

    # Load the image using Pillow
    img = Image.open(input_path)

    # Resize the image
    resized_img = img.resize(new_size)

    # Save the resized image to the output path
    resized_img.save(output_path)

if __name__ == "__main__":
    ORIGINAL_DIRECTORY = "dataset\\raw-img"
    NEW_DIRECTORY = "dataset64"
    NEW_IMAGE_SIZE = (64, 64)

    contents = os.listdir(ORIGINAL_DIRECTORY)

    # Filter out only the directories
    folders = [item for item in contents if os.path.isdir(os.path.join(ORIGINAL_DIRECTORY, item))]

    # Loops through all folders and add modified copies to new directory
    for folder in folders:
        folder_path = os.path.join(ORIGINAL_DIRECTORY, folder)

        # Display folder currently being modified
        print(f"Current folder: {folder_path}")

        image_names = os.listdir(folder_path)

        # Creates folder if folder does not exist
        if not os.path.exists(os.path.join(NEW_DIRECTORY, folder)):
            os.makedirs(os.path.join(NEW_DIRECTORY, folder))

        # Loops through all images and then resizes them and stores them into the new directory
        for image_name in image_names:
            file_original_path = os.path.join(ORIGINAL_DIRECTORY, folder, image_name)
            file_new_path = os.path.join(NEW_DIRECTORY, folder, image_name)

            resize_and_store_image(file_original_path, file_new_path, NEW_IMAGE_SIZE)
