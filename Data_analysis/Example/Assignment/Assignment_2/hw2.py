import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

torch.manual_seed(42)

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 10)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = x.view(-1, 784)
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x

def evaluate(model, loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in loader:
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    return 100 * correct / total

def train_and_evaluate(config, show_plot=True):
    batch_size, num_epochs, learning_rate = config
    
    transform = transforms.ToTensor()
    train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)
    test_dataset = datasets.MNIST(root='./data', train=False, transform=transform, download=True)
    train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)
    
    model = Net()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=learning_rate)
    
    losses = []
    for epoch in range(num_epochs):
        epoch_loss = 0.0
        for images, labels in train_loader:
            outputs = model(images)
            loss = criterion(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            epoch_loss += loss.item()
        
        avg_loss = epoch_loss / len(train_loader)
        losses.append(avg_loss)
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {avg_loss:.4f}')

    if show_plot:
        plt.figure(figsize=(8, 5))
        plt.plot(range(1, num_epochs+1), losses, marker='o')
        plt.xlabel('Epoch')
        plt.ylabel('Training Loss')
        plt.title(f'Training Loss (batch_size={batch_size}, lr={learning_rate})')
        plt.grid(True)
        plt.show()

    train_acc = evaluate(model, train_loader)
    test_acc = evaluate(model, test_loader)
    print(f'Training Accuracy: {train_acc:.2f}%')
    print(f'Test Accuracy: {test_acc:.2f}%')
    
    return train_acc, test_acc, losses

configurations = [
    (32, 20, 0.1),
    (32, 20, 1.0),
    (32, 20, 0.01),
    (8, 20, 0.1),
    (128, 20, 0.1)
]

results = {}
for i, config in enumerate(configurations):
    print(f"\n=== Experiment Configuration {chr(97+i)}: batch_size={config[0]}, lr={config[2]} ===")
    train_acc, test_acc, losses = train_and_evaluate(config)
    results[chr(97+i)] = {
        'batch_size': config[0],
        'learning_rate': config[2],
        'train_acc': train_acc,
        'test_acc': test_acc,
        'losses': losses
    }

print("\n=== Analysis Results ===")

print("\n1. Impact of Learning Rate:")
print("High learning rate (1.0) causes large fluctuations in training loss, making convergence difficult or unstable")
print("Low learning rate (0.01) results in slow decrease of training loss and slow convergence")
print("Moderate learning rate (0.1) typically achieves good convergence")

print("\n2. Impact of Batch Size:")
print("Small batch size (8) introduces more noise in training, with more fluctuation in loss curve, but may help generalization")
print("Large batch size (128) makes training more stable with smoother loss curve, but may get stuck in local optima")
print("Moderate batch size (32) achieves a good balance between stability and generalization")

print("\n=== Results Summary ===")
print("Config | Batch Size | Learning Rate | Train Acc | Test Acc")
print("-------|------------|---------------|-----------|---------")
for key, val in results.items():
    print(f"{key}      | {val['batch_size']:10} | {val['learning_rate']:13} | {val['train_acc']:8.2f}% | {val['test_acc']:7.2f}%")