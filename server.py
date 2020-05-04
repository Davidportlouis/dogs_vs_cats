from flask import Flask,render_template,request
from PIL import Image
import torch
from torch import nn
from torchvision import transforms
import matplotlib.pyplot as plt
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/uploads/'

model = torch.load('checkpoint.pth')

def apply_test_transforms(inp):
    out = transforms.functional.resize(inp, [224,224])
    out = transforms.functional.to_tensor(out)
    out = transforms.functional.normalize(out, [0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    return out

def pred_class(image):
    img = Image.open(image)
    img_tensor = apply_test_transforms(img)
    softMax = nn.Softmax(dim = 1)
    batch = torch.stack([img_tensor])
    preds = softMax(model(batch))
    return (preds[0,0].item(),preds[0,1].item())


@app.route('/')
def index():
    return render_template('index.html',title="Home")

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        f = request.files['image']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
        predict = pred_class('./static/uploads/' + f.filename)
        return render_template('predict.html',img=f.filename,cat=round(predict[0]*100,2),dog=round(predict[1]*100,2),title="Prediction")

if __name__ == "__main__":
    app.run(debug=True)