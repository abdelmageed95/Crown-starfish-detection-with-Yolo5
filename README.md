Crown-starfish-detection
=======================================
### Dataset
The Dataset was acquired from 17 YouTube, at the end we got 725 images.And using data augmentation we increased the number of images to 2548. 
### Pipline
- Image annotation
- Image Preprocessing: we used  white balance enhancement technique 
• lighten dark images
• solve the greenish-blue appearance
<img src="images\output.png" hight="20px">
-Image Augmentation
--------------------------------
### Models Results
-Basic Model
Test Sample             |  Train
:-------------------------:|:-------------------------:
<img src="results\exp9\1403326938.jpg" width="500px" hight="500px"/>  |  ![](notebook\original\mAP.PNG)

-Preprocessed Model
Test Sample             |  Train
:-------------------------:|:-------------------------:
<img src="results\exp11\1403326938.jpg" width="500px" hight="500px"/>  |  ![](notebook\preprocessing\mAP.PNG)

-Augmented Model
Test Sample             |  Train
:-------------------------:|:-------------------------:
<img src="results\exp10\1403326938.jpg" width="500px" hight="500px"/>  |  ![](notebook\original\mAP.PNG)

### DEMO
we used Flak API to deploy our model.
[![run](https://img.youtube.com/vi/DeSbxpgxe_I/0.jpg)](https://www.youtube.com/embed/DeSbxpgxe_I)
