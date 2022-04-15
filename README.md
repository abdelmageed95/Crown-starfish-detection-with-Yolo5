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

• Image Augmentation


### Models Results

-Basic Model


<img src="images\1.jpg" width="500px" hight="500px"/> 

-Preprocessed Model

<img src="images\2.jpeg" width="500px" hight="500px"/>  

-Augmented Model

<img src="images\3.jpeg" width="500px" hight="500px"/> 

### DEMO
we used Flak API to deploy our model.

[![run](https://img.youtube.com/vi/DeSbxpgxe_I/0.jpg)](https://www.youtube.com/embed/DeSbxpgxe_I)



steps to run the code:
 - Clone the repo
 - pip install requirements.txt 
 - Run the application file " ../Crown-starfish-detection-with-Yolo5/yolov5/app.py"
 - click the link that will appear and choose an image or vedio 
 - The results will be saved in  " ../Crown-starfish-detection-with-Yolo5/results"


## Note :
" you will need to change the paths in  " ..\Crown-starfish-detection-with-Yolo5\yolov5\app.py"
 and " ..\Crown-starfish-detection-with-Yolo5\yolov5\detect.py" to your absolute path

