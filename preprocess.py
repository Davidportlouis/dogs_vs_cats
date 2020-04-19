# warning: run only once for preprocessing  
import os
import re
import shutil

train_dir = "data/train/"
val_dir = "data/val/"
test_dir = "data/test/"

# creating new directories for individual classes
os.mkdir(train_dir+'dog')
os.mkdir(train_dir+'cat')
os.mkdir(val_dir+'dog')
os.mkdir(val_dir+'cat')

# splitting the classes to separate directories
images = os.listdir(train_dir)

for img in images:
    cat = re.search("cat",img)
    dog = re.search("dog",img)
    if cat:
        shutil.move(f"{train_dir}/{img}",train_dir+'cat/')
    else:
        shutil.move(f"{train_dir}/{img}",train_dir+'dog/')

# # holding out images for validation

cat_img = os.listdir(train_dir+'cat')

for img in cat_img:
    cat = re.search("5\d\d\d",img)
    shutil.move(f"{train_dir}/cat/{img}",val_dir+'cat/')

dog_img = os.listdir(train_dir+'dog')

for img in dog_img:
    dog = re.search("5\d\d\d",img)
    shutil.move(f"{train_dir}/dog/{img}",val_dir+'dog/')