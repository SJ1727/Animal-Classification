import torch.nn as nn
import torch

class AnimalClassificationNeuralNet(nn.Module):
    def __init__(self, in_channels, out_features):
        super().__init__()

        self.net = nn.Sequential(
            nn.Conv2d(in_channels, 20, 5), # 20 x 60 x 60
            nn.MaxPool2d(2), # 20 x 30 x 30
            nn.Conv2d(20, 40, 3), # 40 x 28 x 28
            nn.MaxPool2d(2), # 40 x 14 x 14
            nn.Conv2d(40, 20, 3), # 20 x 12 x 12
            nn.MaxPool2d(2), # 20 x 6 x 6
            nn.Flatten(),
            nn.Linear(20 * 6 * 6, 16),
            nn.Linear(16, out_features),
            nn.Sigmoid(),
        )

    def forward(self, x):
        return self.net(x)