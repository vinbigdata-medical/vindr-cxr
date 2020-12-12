import torch
from torchvision import models
import torch.nn as nn
from PIL import Image
from torch import optim, cuda
from .transforms import *
from .config import WEIGHT


class OutlierDetector():

    def __init__(self, device="cuda:0", weight=WEIGHT):

        self.model = models.resnet18(pretrained=False)
        self.num_features = self.model.fc.in_features
        self.model.fc = nn.Linear(self.num_features, 2)
        self.model.load_state_dict(torch.load(weight))
        self.model.eval()
        
        if not torch.cuda.is_available():
            device = "cpu"
            
        self.model = self.model.to(device)
        self.model = nn.DataParallel(self.model)
        self.device = device


    def forward(self, image):
        
        image = image.to(self.device)
        
        with torch.no_grad():
          output = self.model.forward(image)
          index = output.data.cpu().numpy().argmax()
         
        torch.cuda.empty_cache()
        
        return index
        
        
    def predict(self, image_path):
        
        image = load_xrayImg(image_path)
        probs = self.forward(image)   
        
        return probs