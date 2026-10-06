import torch 
import torch.nn as nn

class MyNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear1 = nn.Linear(784, 256)
        self.relu1 = nn.ReLU()
        self.dropout1 = nn.Dropout(p=0.2)
        self.linear2 = nn.Linear(256, 128)
        self.dropout2 = nn.Dropout(p=0.2)
        self.relu2 = nn.ReLU()
        self.linear3 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.flatten(x)
        x = self.linear1(x)
        x = self.relu1(x)
        x = self.dropout1(x)
        x = self.linear2(x)
        x = self.dropout2(x)
        x = self.relu2(x)
        x = self.linear3(x)

        return x
    