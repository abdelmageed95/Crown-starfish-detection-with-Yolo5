from re import DEBUG, sub
from flask import Flask, render_template, request,jsonify
import os
from base64 import b64encode

app = Flask(__name__)

uploads_dir = os.path.join(app.instance_path, 'uploads')
from detect import run_test


os.makedirs(uploads_dir, exist_ok=True)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/detect", methods=['POST'])
def detect():
    video = request.files['video']
    video.save(os.path.join(uploads_dir, (video.filename)))
    obj = (video.filename)
    input_path = str(os.path.join(uploads_dir, obj))
    path_original,path_preprocessing,path_augemented = run_test(input_path)
    with open(os.path.join(r"..\Crown-starfish-detection-with-Yolo5",path_original), "rb") as f:
        image_binary = f.read()
    image_original = b64encode(image_binary).decode("utf-8")
    with open(os.path.join(r"..\Crown-starfish-detection-with-Yolo5",path_preprocessing), "rb") as f:
        image_binary = f.read()
    image_preprocessing = b64encode(image_binary).decode("utf-8")
    with open(os.path.join(r"..\Crown-starfish-detection-with-Yolo5",path_augemented), "rb") as f:
        image_binary = f.read()
    image_augemented = b64encode(image_binary).decode("utf-8")
    return jsonify({'status': True, 'image_original': image_original,'image_preprocessing': image_preprocessing,'image_augemented':image_augemented})

if __name__ == '__main__':
    app.run(port=5000,debug=True)