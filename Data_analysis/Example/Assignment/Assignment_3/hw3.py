import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from multiprocessing import Pool, freeze_support
from torch.utils.data import RandomSampler

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

def average_models(models):
    model_params = [model.state_dict() for model in models]
    averaged_params = {}
    
    for param_name in model_params[0]:
        params = torch.stack([model_params[i][param_name] for i in range(len(models))])
        averaged_params[param_name] = torch.mean(params, dim=0)
    
    return averaged_params

def duplicate_model(model, num_duplicates):
    model_dicts = [model.state_dict() for _ in range(num_duplicates)]
    duplicated_models = [Net() for _ in range(num_duplicates)]
    for i, model_dict in enumerate(model_dicts):
        duplicated_models[i].load_state_dict(model_dict)
    return duplicated_models

def train_model(args):
    model, optimizer, criterion, random_sampler, batch_size = args
    
    train_loader_random = torch.utils.data.DataLoader(
        dataset=random_sampler.data_source,
        batch_size=batch_size,
        sampler=random_sampler
    )
    
    total_loss = 0
    model.train()
    
    for i, (images, labels) in enumerate(train_loader_random):
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    
    return model, total_loss

def run_experiment(config):
    batch_size = config['batch_size']
    num_communications = config['num_communications']
    learning_rate = config['learning_rate']
    num_workers = config['num_workers']
    num_local_steps = config['num_local_steps']
    
    train_dataset = datasets.MNIST(root='./data', train=True, transform=transforms.ToTensor(), download=True)
    test_dataset = datasets.MNIST(root='./data', train=False, transform=transforms.ToTensor())
    
    criterion = nn.CrossEntropyLoss()
    
    train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
    random_sampler = RandomSampler(
        data_source=train_dataset,
        replacement=True,
        num_samples=num_local_steps * len(train_loader)
    )
    
    losses_array = []
    model = Net()
    
    for _ in range(num_communications):
        models = duplicate_model(model, num_workers)
        optimizers = [optim.SGD(model.parameters(), lr=learning_rate) for model in models]
        
        args_list = [(models[i], optimizers[i], criterion, random_sampler, batch_size) 
                     for i in range(num_workers)]
        
        with Pool(num_workers) as pool:
            results = pool.map(train_model, args_list)
        
        models = [result[0] for result in results]
        total_loss = sum(result[1] for result in results)
        
        ensemble_model_params = average_models(models)
        model.load_state_dict(ensemble_model_params)
        
        losses_array.append(total_loss)
    
    plt.figure(figsize=(10, 6))
    plt.plot(losses_array)
    plt.xlabel('Communication Rounds')
    plt.ylabel('Total Loss')
    plt.title(f"Training Loss - Workers: {num_workers}, Local Steps: {num_local_steps}")
    plt.show()
    
    model.eval()
    with torch.no_grad():
        correct = 0
        total = 0
        for images, labels in train_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
        train_accuracy = 100 * correct / total
    
    test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)
    model.eval()
    with torch.no_grad():
        correct = 0
        total = 0
        for images, labels in test_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
        test_accuracy = 100 * correct / total
    
    print(f"Configuration: {config}")
    print(f"Training Accuracy: {train_accuracy:.2f}%")
    print(f"Test Accuracy: {test_accuracy:.2f}%")
    print("="*50)
    
    return {
        'config': config,
        'train_accuracy': train_accuracy,
        'test_accuracy': test_accuracy,
        'losses': losses_array
    }

if __name__ == '__main__':
    freeze_support()
    
    configurations = [
        {
            'batch_size': 32,
            'num_communications': 50,
            'learning_rate': 0.1,
            'num_workers': 2,
            'num_local_steps': 5
        },
        {
            'batch_size': 32,
            'num_communications': 50,
            'learning_rate': 0.1,
            'num_workers': 4,
            'num_local_steps': 5
        },
        {
            'batch_size': 32,
            'num_communications': 50,
            'learning_rate': 0.1,
            'num_workers': 8,
            'num_local_steps': 5
        },
        {
            'batch_size': 32,
            'num_communications': 50,
            'learning_rate': 0.1,
            'num_workers': 4,
            'num_local_steps': 20
        }
    ]

    results = []
    for config in configurations:
        results.append(run_experiment(config))