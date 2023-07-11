import cv2
import argparse
import math

def resize(input_image, output_image, desired_size):
    if not(input_image.lower().endswith('.png')):
        raise Exception("Please provide a filename with a .png extension for the input file.")
    if not(output_image.lower().endswith('.png')):
        raise Exception("Please provide a filename with a .png extension for the output file.")
    if not(type(desired_size) == int):
        raise Exception("Please provide the desired size in integer format.")
    input_img = cv2.imread(input_image, cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(input_img, (desired_size, desired_size))
    cv2.imwrite(output_image, resized_image)

def main():
    parser = argparse.ArgumentParser(description="This is a command-line tool to resize an image.")
    parser.add_argument("-i", "--INPUT_DATA_PATH", help="path/to/your/input.png", type=str, required=True)
    parser.add_argument("-o", "--OUTPUT_DATA_PATH", help="path/to/your/output.png", type=str, required=True)
    parser.add_argument("-s", "--SIZE", help="desired output size of your input", type=int, default=256, required=False)
    args = parser.parse_args()
    resize(args.INPUT_DATA_PATH, args.OUTPUT_DATA_PATH, args.SIZE)

if __name__ == "__main__":
    main()
