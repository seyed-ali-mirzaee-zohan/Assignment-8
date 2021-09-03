import imageio
import os
files = os.listdir('picture')
images=[]
for i in range (len(files)):
    image=imageio.imread('picture/'+files[i])
    images.append(image)
imageio.mimsave('copperplate.gif',images)  