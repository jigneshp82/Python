import torch
import torchvision.transforms as transforms
import torch.nn as nn
import torchvision.datasets as datasets
import numpy as np

IMAGESIZE = 16



print (IMAGESIZE)
train_data = datasets.MNIST(root = './data',train =  True, download = True, transform = transforms.ToTensor())