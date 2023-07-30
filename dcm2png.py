# dcm2png.py -- Convert DICOM to PNG format

import pydicom
import cv2
import argparse
from pydicom.pixel_data_handlers.util import apply_voi_lut
import numpy as np
import os


def DCM2PNG(input_path: str, brightness: float, output_path: str) -> None:
    for dcmFile in os.listdir(input_path):
        file_path = os.path.join(input_path, dcmFile)
        if not os.path.isfile(file_path):
            continue  # Skip if it's not a file
        try:
            dcm = pydicom.dcmread(file_path)
            if "VOILUTSequence" in dcm:
                png = apply_voi_lut(dcm.pixel_array, dcm)
            else:
                png = dcm.pixel_array.astype(np.float32) * brightness

            cv2.imwrite(os.path.join(output_path, os.path.splitext(dcmFile)[0] + ".png"), png)
        except pydicom.errors.InvalidDicomError:
            print(f"Skipping non-DICOM file: {dcmFile}")
            
            
def main() -> None:
    parser = argparse.ArgumentParser(description="This is a command-line tool for"
                                                 " performing DICOM file to PNG file conversion.")
    parser.add_argument("-i", "--INPUT_DATA_PATH", help="path/to/your/input/dcm/directory", type=str, required=True)
    parser.add_argument("-b", "--BRIGHTNESS", help="adjust brightness of your output file", type=float, default=0.2, required=False)
    parser.add_argument("-o", "--OUTPUT_DATA_PATH", help="path/to/your/output/png/directory", type=str, required=True)
    args = parser.parse_args()
    DCM2PNG(args.INPUT_DATA_PATH, args.BRIGHTNESS, args.OUTPUT_DATA_PATH)


if __name__ == '__main__':
    main()
