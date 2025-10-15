import torch
import torch.nn as nn
from PIL import Image
import torchvision.transforms as transforms
import timm

# Load Xception base model
model = timm.create_model('xception', pretrained=False)

# Modify final layer to match saved model (1 output for binary classification)
model.fc = nn.Linear(model.fc.in_features, 1)

# Load weights
model.load_state_dict(torch.load(r"C:\VS Code\Jupyter Notebook\deepfake_model1.pt", map_location=torch.device('cpu')))
model.eval()

def predict_image(image: Image.Image):
    transform = transforms.Compose([
        transforms.Resize((299, 299)),
        transforms.ToTensor(),
        transforms.Normalize([0.5]*3, [0.5]*3)
    ])
    img_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = model(img_tensor)
        prob = torch.sigmoid(output).item()
        label = "Fake" if prob > 0.5 else "Real"
        confidence = prob if label == "Fake" else 1 - prob
        return label, confidence