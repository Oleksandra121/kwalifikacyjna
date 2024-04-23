import torch
import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(10, 2)  
    def forward(self, x):
        return self.linear(x)


model = SimpleModel()


test_input = torch.randn(1, 10)


output = model(test_input)


torch.save(model.state_dict(), 'model.pt')
print("Модель збережена як model.pt")