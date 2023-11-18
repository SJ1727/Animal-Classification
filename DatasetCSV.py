import csv
import os

def insert_into_csv(csv_filename, data):
    """
    Create a CSV file with columns: image_path, label, human_label.

    - csv_filename (str): The name of the CSV file to be inserted into.
    - data (list of tuples): A list of tuples where each tuple contains (image_path, label, human_label).
    """
    with open(csv_filename, 'a', newline='') as csvfile:
        fieldnames = ['image_path', 'label', 'human_label']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for row in data:
            writer.writerow({'image_path': row[0], 'label': row[1], 'human_label': row[2]})

if __name__ == "__main__":

    labels = {
        "butterfly" : 0,
        "cat" : 1,
        "chicken" : 2,
        "cow" : 3,
        "dog" : 4,
        "elephant" : 5,
        "horse" : 6,
        "sheep" : 7,
        "spider" : 8,
        "squirrel" : 9,
    }


    DIRECTORY = "dataset64"
    CSV_PATH = "dataset64\ImageLabels.csv"

    contents = os.listdir(DIRECTORY)

    # Filter out only the directories
    folders = [item for item in contents if os.path.isdir(os.path.join(DIRECTORY, item))]

    # Loops through all folders and add modified copies to new directory
    for folder in folders:
        folder_path = os.path.join(DIRECTORY, folder)

        # Display folder currently being modified
        print(f"Current folder: {folder_path}")

        image_names = os.listdir(folder_path)

        # Loops through all images and stores data into csv
        # Data in format: image_path, label, human_label
        insert_into_csv(
            CSV_PATH, 
            tuple(
                (
                os.path.join(DIRECTORY, folder, image_name), 
                labels[folder],
                folder
                )
                for image_name in image_names
            )
        )

