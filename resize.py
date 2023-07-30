import cv2
import argparse
import os

def resize(input_directory, output_directory, desired_size):
    if not(type(desired_size) == int):
        raise Exception("Please provide the desired size in integer format.")
    for pngFile in os.listdir(input_directory):
        input_image = cv2.imread(os.path.join(input_directory, pngFile), cv2.IMREAD_GRAYSCALE)
        resized_image = cv2.resize(input_image, (desired_size, desired_size))
        print(os.path.join(output_directory, pngFile))
        cv2.imwrite(os.path.join(output_directory, os.path.splitext(pngFile)[0] + "_" + str(desired_size) + ".png"), resized_image)

def main():
    parser = argparse.ArgumentParser(description="This is a command-line tool to resize a series of images in a specific directory.")
    parser.add_argument("-i", "--INPUT_DATA_PATH", help="path/to/your/input/directory", type=str, default="png_files", required=False)
    parser.add_argument("-o", "--OUTPUT_DATA_PATH", help="path/to/your/output/directory", type=str, required=True)
    parser.add_argument("-s", "--SIZE", help="desired output size of your input", type=int, default=640, required=False)
    args = parser.parse_args()
    resize(args.INPUT_DATA_PATH, args.OUTPUT_DATA_PATH, args.SIZE)

if __name__ == "__main__":
    main()
