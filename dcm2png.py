import pydicom
import cv2
import argparse





def dcm_to_png(dicom_filename, png_filename):
    pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="path/to/your/file.dcm", required=True)
    parser.add_argument("-o", "--output", help="path/to/your/output.png", required=True)


    args = parser.parse_args()
    dcm_to_png(args.input, args.output)


if __name__ == '__main__':
    main()