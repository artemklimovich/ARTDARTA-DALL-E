# -*- coding: utf-8 -*-
"""ARTDARTA-DALL-E: CLIP+DALL-E decoder.ipynb"

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/artemklimovich/f847c39e9a60bf74ad1d1c2c024a9c80/artdarta-dall-e-clip-dall-e-decoder-ipynb.ipynb

# ARTDARTA-DALL-E






---

#### What is this?

This is a notepad that uses a decoder to work with the DALL-E neural network and CLIP to create images from text. The best images created are used to create NFT tokens in the [Artificial Intelligence Machine Art](https://opensea.io/collection/aiartmachine) collection in OpenSea. As the project evolves, we will make it simpler, better, and more user-friendly.

Feel free to send correspondence to [@KlimovichArtem](https://twitter.com/KlimovichArtem) on Twitter. If you use this notebook or modify it, please be cool and link back to my twitter. 

The notebook was created with tremendous help from [@advadnoun](https://twitter.com/advadnoun)



---

#### Thanks!

Many thanks to OpenAI for releasing their models CLIP and DALL-E (the encoder and decoder parts, specifically). I am not affiliated with them.


Original https://github.com/openai/DALL-E/ (Aditya Ramesh, Mikhail Pavlov, Gabriel Goh, Scott Gray, Chelsea Voss, Alec Radford, Mark Chen, Ilya Sutskever). Clone https://github.com/artemklimovich/ARTDARTA-DALL-E

Original https://github.com/openai/CLIP (Alec Radford, \* Jong Wook Kim,\* Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal,
Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, Ilya Sutskever). Clone https://github.com/artemklimovich/ARTDARTA-DALL-E/tree/master/CLIP

\* equal contribution

Also, as a good launching point for future directions and to find more related work, see https://distill.pub/2017/feature-visualization/ by Chris Olah, Alexander Mordvintsev, Ludwig Schubert.



---

# How do I use this?

First, type in your description where it says *Insert text here*.


Second, click the ![image.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA/CAYAAABTqsDiAAAEhklEQVRoBeWbx07rUBCG82xsYQtbeBB4CPYUsWAHQkiwAIEQsEGigwDRe++9M1efpYkOTmIf7NjXZfHLCY6P/Z0pZ4zHhZ+fH/n+/i7R19eXuPX5+SlZUAFoU+4JyCL4L2gT2IR1W/fj40P89P7+LklVEbocsMKagG6Qt7c3SZsc6ErACmuCmoCvr6+SRhXcwKZ1gQUSsJeXF3l6enL0+PgoqoeHB0mbitAaw0ADa4ICCNj9/b3c3d3J7e2to5ubGzF1fX0taZADbQKrZZ+fn2Vvby8TcodgERoLa7wCjFUzC61WJmkBDTCufHV1lW1oM46JX+L05OQk29CmlXHr8/PzzAAToiUxjXsDzQ618vHxsWxsbGQGvARaXZt1WGP54OBAVldXswuNlVmXgca1Ly4uHNilpaV8QFN4EM87OzsyPz+ffWiWKqDPzs5ke3s7H9DU1UCfnp7K1taWzM7OZtvSFCW5heZGQi09MzMTmaWHhoakr69PWltbHfGZv0VV9pYsWVqYYGkqMaA3Nzel2tATExPS0tIidXV1UlNTU1bs4zf8tpoTUAKt98xRQbPeA1IJtNLfOaZatUKs0FisoaHhz8A6ERxbDavHBs3FermygvltGSMseCzQuGUYC7sngrHCuHos0M3NzYFd2g2s3xkzaHKLHBpX1AuttG1sbJTa2lrf37mPD7qiRA5tY2XWZyYHeDeY1/eg1o4c2saCQOOqxKnNJOlEkNSCuHik0FRVeoFeW4VWgO7ubmt3D1K5RQpNOekFq/vc0MDbujvn0Mmy3UYKDYyCeW3LQQNg4+6VjvWagMRD+5WsiYMO695NTU2+npI49w6TyGxL1sQlMuLqr0uWnzubuYGxvWK30r5IY5qT2qy7xCXZ2sadTejEFic2ZSiwtu5sQie2DLW1tglj8zmolbmeyN2bk7De1tfX+2ZiG1h+w1iJv7UEHDe3SWp+4IzBWIwZVLFYWi+Oiw1jcY4NC8y1xArNCW1Ky3LWJobDuLRO/H+B1pNjMUC8XJ59/CZoltZzubcllo7r/97mhVBVUU6yXiM+B6m0zDG9PntCx/WEw+sCo9hnDZ35B3g85eAJh2npXEHzfDoXj2qxNA/lsbQ+lJ+bmwtcDEQRl2HGLBvTCm12IuQKOhc9J7RUsVab3UW7u7uysLCQXfd2Q19eXsr+/r4sLy9nH5pgZ9miX/vw8FDW1tayDY21tdmGFgzaJFm26CUbHx+XwcFB6enpEZ5EdHV1SWdnp3R0dEh7e3uJ2traJOkq0BtqtkqaXYPc5UxPTzvgw8PDMjAwIP39/U6t3NvbKyomJE1yoLUplmRGUywujrVpoltZWXF6yqampmRyctKZgLGxMRkdHXU0MjIiaVOxs1/vtrRzkIQGOJl8fX3dgV9cXHSyOiWqitvAtMl5Rcl0cU1oFCqAU6GR2KiIsDyiLdoUk5ImFd/LMsHVzQEnsQFP0UKPGcIDjo6OrMWkJUm/3sBTcDI5Ftf3OUhuOgHmK0i855FG/YLmxTQyuRYsCo/lmQDWcbdIfGnTPyMBsv9CTWMwAAAAAElFTkSuQmCC) 
button that shows up next to the text under the heading **This one!**. The button appears when you move your mouse over the text **This one!** Wait for a bit as it loads and goes in circles, and then move on to the third step when it finishes running.

Third, click on the upper bar at the top of the page where it says **Runtime**, and then click **Restart and run all**. 

Your output will appear at the bottom of this page as it trains after a little while. Scroll down below everything else to see new images appear. The images will start by looking like dirt, but the page will eventually ding and show new images as it begins to attempt to match the image to your description.

# Choose Text
"""

text_input = '''god'''

"""# This one!"""

import subprocess

CUDA_version = [s for s in subprocess.check_output(["nvcc", "--version"]).decode("UTF-8").split(", ") if s.startswith("release")][0].split(" ")[-1]
print("CUDA version:", CUDA_version)

if CUDA_version == "10.0":
    torch_version_suffix = "+cu100"
elif CUDA_version == "10.1":
    torch_version_suffix = "+cu101"
elif CUDA_version == "10.2":
    torch_version_suffix = ""
else:
    torch_version_suffix = "+cu110"

!pip install torch==1.7.1{torch_version_suffix} torchvision==0.8.2{torch_version_suffix} -f https://download.pytorch.org/whl/torch_stable.html ftfy regex

"""# Top

"""

# don't use half of these lol

import torch
import numpy as np
import torchvision
import torchvision.transforms.functional as TF

import PIL
import matplotlib.pyplot as plt

import os
import random
import imageio
from IPython import display
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import glob

from google.colab import output

# were you lucky today?

!nvidia-smi -L

"""# Perceptor"""

# Commented out IPython magic to ensure Python compatibility.


# %cd /content/

!git clone https://github.com/artemklimovich/ARTDARTA-CLIP.git


# %cd /content/CLIP/

!pip install ftfy

import os
import CLIP
import torch

clip.available_models()

import numpy as np

# Load the model
perceptor, preprocess = clip.load('ViT-B/32', jit=True)
perceptor = perceptor.eval()



"""# Params"""

# probably don't mess with this unless you're changing generator size
im_shape = [512, 512, 3]
sideX, sideY, channels = im_shape
batch_size = 1

"""# Define"""

def displ(img, pre_scaled=True):
  img = np.array(img)[:,:,:]
  img = np.transpose(img, (1, 2, 0))
  if not pre_scaled:
    img = scale(img, 48*4, 32*4)
  imageio.imwrite(str(3) + '.png', np.array(img))
  return display.Image(str(3)+'.png')

def gallery(array, ncols=2):
    nindex, height, width, intensity = array.shape
    nrows = nindex//ncols
    assert nindex == nrows*ncols
    # want result.shape = (height*nrows, width*ncols, intensity)
    result = (array.reshape(nrows, ncols, height, width, intensity)
              .swapaxes(1,2)
              .reshape(height*nrows, width*ncols, intensity))
    return result

def card_padded(im, to_pad=3):
  return np.pad(np.pad(np.pad(im, [[1,1], [1,1], [0,0]],constant_values=0), [[2,2], [2,2], [0,0]],constant_values=1),
            [[to_pad,to_pad], [to_pad,to_pad], [0,0]],constant_values=0)

def get_all(img):
  img = np.transpose(img, (0,2,3,1))
  cards = np.zeros((img.shape[0], sideX+12, sideY+12, 3))
  for i in range(len(img)):
    cards[i] = card_padded(img[i])
  print(img.shape)
  cards = gallery(cards)
  imageio.imwrite(str(3) + '.png', np.array(cards))
  return display.Image(str(3)+'.png')

"""# Generator"""

import io
import os, sys
import requests
import PIL

import torch
import torchvision.transforms as T
import torchvision.transforms.functional as TF

!pip install git+https://github.com/artemklimovich/ARTDARTA-DALL-E.git


from dall_e import map_pixels, unmap_pixels, load_model
target_image_size = sideX

def preprocess(img):
    s = min(img.size)
    
    if s < target_image_size:
        raise ValueError(f'min dim for image {s} < {target_image_size}')
        
    r = target_image_size / s
    s = (round(r * img.size[1]), round(r * img.size[0]))
    img = TF.resize(img, s, interpolation=PIL.Image.LANCZOS)
    img = TF.center_crop(img, output_size=2 * [target_image_size])
    img = torch.unsqueeze(T.ToTensor()(img), 0)
    return map_pixels(img)


model = load_model("https://cdn.openai.com/dall-e/decoder.pkl", 'cuda')
encoder = load_model("https://cdn.openai.com/dall-e/encoder.pkl", 'cuda')

oi = encoder(map_pixels(.2*torch.nn.functional.interpolate(torch.rand(1, 3, sideX//4, sideY//4), (sideX, sideY))).cuda())



"""# Latent coordinates"""

class Pars(torch.nn.Module):
    def __init__(self):
        super(Pars, self).__init__()


        hots = torch.nn.functional.one_hot((torch.arange(0, 8192).to(torch.int64)), num_classes=8192)
        rng = torch.zeros(batch_size, 64*64, 8192).uniform_()**torch.zeros(batch_size, 64*64, 8192).uniform_(.1,1)
        for b in range(batch_size):
          for i in range(64**2):
            rng[b,i] = hots[[np.random.randint(8191)]]

        rng = rng.permute(0, 2, 1)

        self.normu = torch.nn.Parameter(rng.cuda().view(batch_size, 8192, 64, 64))

        # ended up not doing static, as the brown seems to actually work better here

        # self.normu = torch.nn.Parameter(oi.cuda().clone())



    def forward(self):

      
      normu = torch.softmax(hadies*self.normu.reshape(batch_size, 8192//2, -1), dim=1).view(batch_size, 8192, 64, 64)
      return normu


lats = Pars().cuda()
mapper = [lats.normu]
optimizer = torch.optim.Adam([{'params': mapper, 'lr': .05}])
eps = 0



tx = clip.tokenize(text_input)
t = perceptor.encode_text(tx.cuda()).detach().clone()


nom = torchvision.transforms.Normalize((0.48145466, 0.4578275, 0.40821073), (0.26862954, 0.26130258, 0.27577711))


will_it = False
hadies = 1.
with torch.no_grad():
  al = unmap_pixels(torch.sigmoid(model(lats()).cpu().float())).numpy()
  for allls in al:
    displ(allls[:3])
    print('\n')
  # print(lats())
  # print(lats().sum())







"""# Train"""

def checkin(loss):
  global hadies
  print('''
  ##########################################################
  ''',
        loss, ' (loss)\n',itt)
  
  with torch.no_grad():
    
    al = unmap_pixels(torch.sigmoid(model(lats())[:, :3]).cpu().float()).numpy()
    for allls in al:
      displ(allls)
      display.display(display.Image(str(3)+'.png'))
      print('\n')



  # the people spoke and they love "ding"
  output.eval_js('new Audio("https://freesound.org/data/previews/80/80921_1022651-lq.ogg").play()')


def ascend_txt():
  out = unmap_pixels(torch.sigmoid(model(lats())[:, :3].float()))

  

  cutn = 64 # improves quality
  p_s = []
  for ch in range(cutn):
    size = int(sideX*torch.zeros(1,).uniform_(.8, .99))#.normal_(mean=.8, std=.3).clip(.5, .98))
    offsetx = torch.randint(0, sideX - size, ())
    offsety = torch.randint(0, sideX - size, ())
    apper = out[:, :, offsetx:offsetx + size, offsety:offsety + size]
    apper = torch.nn.functional.interpolate(apper, (224,224), mode='bilinear')
    p_s.append(apper)
  into = torch.cat(p_s, 0)
  # into = torch.nn.functional.interpolate(out, (224,224), mode='bilinear')

  into = into + .2 * random.random() * torch.randn_like(into)

  into = nom((into))


  iii = perceptor.encode_image(into)


  lat_l = 0



  return [lat_l, 10*-torch.cosine_similarity(t, iii).view(-1, batch_size).T.mean(1)]

def train(i):
  global hadies
  loss1 = ascend_txt()
  loss = loss1[0] + loss1[1]
  loss = loss.mean()
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()
  
  # hadies /= 1.01
  # hadies = max(hadies, 1.5)

  for g in optimizer.param_groups:
    g['lr'] = g['lr']*1.005
    
  
  if itt % 50 == 0:
    # print('temp', hadies)
    # print(g['lr'], 'lr')
    checkin(loss1)


itt = 0
for asatreat in range(10000):
  train(itt)
  itt+=1







"""# Sharpie"""

hadies = 130000000
will_it = True

with torch.no_grad():
  lll = lats()
  al = unmap_pixels(torch.sigmoid(model(lll)[:, :3]).cpu().float()).numpy()
  for allls in al:
    displ(allls)
    print('\n')

  # print(lll)
  # print(torch.sum(lll))
  displ(torch.topk(lll.view(batch_size, 8192, 64, 64), k=3, dim=1)[0].cpu().numpy()[0])

print(lats())