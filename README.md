#### Binary image classifier for classifying dog vs cats 

![Cat vs Dog](./assets/cat_dog.jpeg)

dataset: ![Dogs vs, Cats | Kaggle](https://www.kaggle.com/c/dogs-vs-cats)
description: Binary image classification to classify dogs and cats
training samples: 20000 images (10000 per class)
validation samples: 50000 images (2500 per class)
testing samples: 12500 unlabelled images 


#### Model Architecture

Pytorch CNN architecture

> (conv_1): Conv2d(3, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
  (conv_2): Conv2d(32, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
  (maxpool): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  (drop): Dropout(p=0.2, inplace=False)
  (fc1): Linear(in_features=160000, out_features=512, bias=True)
  (out): Linear(in_features=512, out_features=2, bias=True)
  
#### metrics
> training loss: 0.392
  validation loss: 0.40058
  test loss: 0.427
  test accuracy: 0.805
  
  
