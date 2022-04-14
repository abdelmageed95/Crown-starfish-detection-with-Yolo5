import numpy as np
from skimage import img_as_ubyte
from PIL import Image
import numpy as np
import os
import cv2
from skimage import img_as_ubyte
from PIL import Image



def load_images_from_folder(folder,num=None):
    images = []
    filenames=[]
    if num:
      dirs = os.listdir(folder)[:num]
    else:
      dirs =  os.listdir(folder)
    for filename in dirs:
        if filename.endswith(".jpg"):
            filenames.append(filename)
            img = Image.open(os.path.join(folder, filename)) # images are color images

            #img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_COLOR)
            # img=cv2.resize(img,(28,28),interpolation=cv2.INTER_AREA)
            if img is not None:
                images.append(img)
    return images,filenames


def whiteBalanced(imgpixels):
  img_max = (imgpixels*0.5 / imgpixels.mean(axis=(0,1)))
  return img_max




def preprocessing(images, Copy_to_path ,filenames):
  for i,img in enumerate(images):
    pixels = np.asarray(img)
    pixels = pixels.astype('float32')
    mean = pixels.mean()
    #outside of our boundary which is least mean
    #and largest mean from the 5 chosen samples will be viewed
    if mean >= 116.930 or mean <= 86.338:
      img_max = whiteBalanced(pixels)
      cv2.imwrite(os.path.join(Copy_to_path,filenames[i]),img_as_ubyte(img_max.clip(0, 1)))


    