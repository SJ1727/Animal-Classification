import os
import torch
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

class AnimalDataset(Dataset):
    def __init__(self, csv_path, transforms=None):
        """
        csv_path (str): Path to csv file containing data
        transform (transforms): Transforms to be applied to data 
        """

        self.data_frame = pd.read_csv(csv_path)
        self.transform = transforms

    def __len__(self):
        return len(self.data_frame)
    
    def __getitem__(self, index):
        if torch.is_tensor(index):
            index = index.tolist()

        image_path = self.data_frame.iloc[index, 0]
        image_label = int(self.data_frame.iloc[index, 1])
        image_human_label = self.data_frame.iloc[index, 2]
        image = Image.open(image_path).convert("RGB")
        sample = [image, image_label, image_human_label]

        if self.transform:
            sample[0] = self.transform(sample[0])

        return sample
    
if __name__ == "__main__":
    print(pd.read_csv("dataset64\ImageLabels.csv").iloc[0, 0])