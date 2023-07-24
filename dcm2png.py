# dcm2png.py -- Convert DICOM to PNG format

import pydicom
import cv2
import argparse
from pydicom.pixel_data_handlers.util import apply_voi_lut
import numpy as np

def dcm_to_png(dicom_filename, brightness, png_filename) -> None:
    if dicom_filename is None:
        raise Exception("Error: No such file or directory")
    if not(dicom_filename.lower().endswith('.dcm')):
        raise Exception("Please provide a filename with a .dcm extension for the input file.")
    if not(png_filename.lower().endswith('.png')):
        raise Exception("Please provide a filename with a .png extension for the output file.")
    dcm = pydicom.dcmread(dicom_filename)
    if "VOILUTSequence" in dicom_filename:
        png_image = apply_voi_lut(dicom_filename.pixel_array, dicom_filename)
    else:
        png_image = dcm.pixel_array.astype(np.float32) * brightness

    cv2.imwrite(png_filename, png_image)

def main() -> None:
    parser = argparse.ArgumentParser(description="This is a command-line tool for"
                                                 " performing DICOM file to PNG file conversion.")
    parser.add_argument("-i", "--INPUT_DATA_PATH", help="path/to/your/input.dcm", type=str, required=True)
    parser.add_argument("-b", "--BRIGHTNESS", help="adjust brightness of your output file", type=float, default=0.2, required=False)
    parser.add_argument("-o", "--OUTPUT_DATA_PATH", help="path/to/your/output.png", default="output.png", required=True)
    args = parser.parse_args()
    dcm_to_png(args.INPUT_DATA_PATH, args.BRIGHTNESS, args.OUTPUT_DATA_PATH)


if __name__ == '__main__':
    main()