import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.datasets as datasets
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
from torch.utils.tensorboard import SummaryWriter  # to print to tensorboard
from model import AnimalClassificationNeuralNet
from dataset import AnimalDataset

writer = SummaryWriter()

BATCH_SIZE = 64
LEARNING_RATE = 1e-3
EPOCHS = 50

# Normilisation for images
transforms = transforms.Compose(
    [
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ]
)

device = "cuda" if torch.cuda.is_available() else "cpu"
net = AnimalClassificationNeuralNet(3, 10)
dataset = AnimalDataset("dataset64\ImageLabels.csv", transforms=transforms)
loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)
net_optim = optim.Adam(net.parameters(), LEARNING_RATE)
criterion = nn.CrossEntropyLoss()
step = 0

for epoch in range(EPOCHS):
    for batch_idx, (images, labels, _) in enumerate(loader):
        # Reshape and put tensors to device
        images = images.to(device)
        labels = labels.view(-1).to(device)

        # Forward pass and gradient calculation
        predictions = net(images)
        net.zero_grad()
        loss = criterion(predictions, labels.long())
        loss.backward()

        # Updating parameters
        net_optim.step()

        # Tensor Board and loss display
        if batch_idx % 20 == 0:
            step += 1

            print(
                f"Epoch [{epoch}/{EPOCHS}] Batch {batch_idx}/{len(loader)} \
                      Loss: {loss:.4f}"
            )

            writer.add_scalar("Loss/train", loss, step)

writer.flush()

torch.save(net.state_dict(), "model.pt")