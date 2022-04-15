from yolov5.detect import main ,parse_opt

if __name__ == "__main__":
    opt = parse_opt(weights_path =r"weights\aug_best.pt",test_images_path=r"C:\Users\alaa\Downloads\Raja Ampat Crown of Thorns Removal Vinegar Injection.mp4",data_yaml="starfish_data/data.yaml")
    main(opt)
