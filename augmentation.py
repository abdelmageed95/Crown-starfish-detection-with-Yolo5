
# requirements 
# %pip install clodsa

from clodsa.augmentors.augmentorFactory import createAugmentor 
from clodsa.transformers.transformerFactory import transformerGenerator 
from clodsa.techniques.techniqueFactory import createTechnique

PROBLEM = "detection"
ANNOTATION_MODE = "yolo"
INPUT_PATH = r"D:\CV_project\starfish_data\train\processed_images"
GENERATION_MODE = "linear"
OUTPUT_MODE = "yolo"
OUTPUT_PATH= r"D:\CV_project\starfish_data\train2"

def apply_augmentation(PROBLEM,ANNOTATION_MODE,OUTPUT_MODE,GENERATION_MODE,INPUT_PATH,OUTPUT_PATH):
    augmentor = createAugmentor(PROBLEM,ANNOTATION_MODE,OUTPUT_MODE,GENERATION_MODE,INPUT_PATH,{"outputPath":OUTPUT_PATH})
    transformer = transformerGenerator(PROBLEM)
    vFlip = createTechnique("flip",{"flip":0})
    augmentor.addTransformer(transformer(vFlip))
    hFlip = createTechnique("flip",{"flip":1})
    augmentor.addTransformer(transformer(hFlip))
    hvFlip = createTechnique("flip",{"flip":-1})
    augmentor.addTransformer(transformer(hvFlip))
    rotate = createTechnique("rotate", {"angle" : 90})
    augmentor.addTransformer(transformer(rotate))
    avgBlur =  createTechnique("average_blurring", {"kernel" : 5})
    augmentor.addTransformer(transformer(avgBlur))
    hue = createTechnique("raise_hue", {"power" : 0.9})
    augmentor.addTransformer(transformer(hue))
    none = createTechnique("none",{})
    augmentor.addTransformer(transformer(none))
    augmentor.applyAugmentation()
    return " Augmentation Done..."