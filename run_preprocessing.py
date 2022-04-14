
from preprocess import  load_images_from_folder ,preprocessing

inputpath   = r"D:\CV_project\starfish_data\train\images"
outputpath  = r"D:\CV_project\starfish_data\train\processed_images"

def enhance(inputpath , outputpath):
    images,filenames = load_images_from_folder(inputpath)
    preprocessing(images,outputpath ,filenames)


enhance(inputpath , outputpath)