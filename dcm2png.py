import pydicom
import cv2
import argparse
from pydicom.pixel_data_handlers.util import apply_voi_lut
import numpy as np



def dcm_to_png(dicom_filename, brightness, png_filename):
    dcm = pydicom.dcmread(dicom_filename)
    if "VOILUTSequence" in dicom_filename:
        png_image = apply_voi_lut(dicom_filename.pixel_array, dicom_filename)
    else:
        png_image = dcm.pixel_array.astype(np.float32) * brightness

    cv2.imwrite(png_filename, png_image)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="path/to/your/input.dcm", type=str, required=True)
    parser.add_argument("-b", "--brightness", help="adjust brightness of your output file", type=float, default=0.2, required=False)
    parser.add_argument("-o", "--output", help="path/to/your/output.png", default="output.png", required=True)

    args = parser.parse_args()
    dcm_to_png(args.input, args.brightness, args.output)


if __name__ == '__main__':
    main()