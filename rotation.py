import cv2
import os
import argparse


def IMG_ROTATE(input_dir, output_dir, rotate_degrees):
    if not(rotate_degrees % 90 == 0):
        raise ValueError("Degrees must be a multiple of 90")

    for imgFile in os.listdir(input_dir):
        src = cv2.imread(os.path.join(input_dir, imgFile), cv2.IMREAD_GRAYSCALE)
        (h, w) = src.shape[:2]
        (cX, cY) = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D((cX, cY), rotate_degrees, 1.0)
        dst = cv2.warpAffine(src, M, (w, h))
        cv2.imwrite(os.path.join(output_dir, imgFile), dst)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--INPUT_DIR", type=str, required=True, help="path/to/your/input/directory")
    parser.add_argument("-o", "--OUTPUT_DIR", type=str, required=True, help="path/to/your/output/directory")
    parser.add_argument("-r", "--ROTATE_DEGREES", type=int, required=False, default=90, help="Rotate degrees")
    args = parser.parse_args()
    IMG_ROTATE(args.INPUT_DIR, args.OUTPUT_DIR, args.ROTATE_DEGREES)
if __name__ == '__main__':
    main()