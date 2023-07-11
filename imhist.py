# imhist.py -- histogram of the png images

import matplotlib.pyplot as plt
import cv2
import argparse
import numpy as np
import os

def imhist(input_filename, show_hist_bool, output_filename):
    if not(input_filename.lower().endswith('.png')):
        raise Exception("Please provide a filename with a .png extension for the input file.")
    if not(output_filename.lower().endswith('.pdf')):
        raise Exception("Please provide a filename with a .pdf extension for the output file.")
    gray_img = cv2.imread(input_filename, cv2.IMREAD_GRAYSCALE)
    if show_hist_bool == 1:
        plt.subplot(1, 2, 1)
        plt.imshow(gray_img, cmap='gray')
        plt.subplots_adjust(wspace=0.5)
        plt.subplot(1, 2, 2)
        plt.hist(gray_img.ravel(), 256, [0, 256], color='blue')
        gray_img_hist, _ = np.histogram(gray_img.flatten(), 256, [0, 256])
        gray_img_CDF = gray_img_hist.cumsum()
        gray_img_CDF_normalized = gray_img_CDF * float(gray_img_hist.max()) / gray_img_CDF.max()
        plt.plot(gray_img_CDF_normalized, color='red')
        plt.legend(('CDF', 'Histogram'), loc='upper right')
        plt.xlabel("Gray-Level Intensity")
        plt.ylabel("Frequency")
        output_filename = os.path.basename(output_filename)
        output_filename = os.path.splitext(output_filename)[0]
        plt.savefig(output_filename + "_hist.pdf")
        plt.show()
    elif show_hist_bool == 0:
        plt.subplot(1, 2, 1)
        plt.imshow(gray_img, cmap='gray')
        plt.subplots_adjust(wspace=0.5)
        plt.subplot(1, 2, 2)
        plt.hist(gray_img.ravel(), 256, [0, 256], color='blue')
        gray_img_hist, _ = np.histogram(gray_img.flatten(), 256, [0, 256])
        gray_img_CDF = gray_img_hist.cumsum()
        gray_img_CDF_normalized = gray_img_CDF * float(gray_img_hist.max()) / gray_img_CDF.max()
        plt.plot(gray_img_CDF_normalized, color='red')
        plt.legend(('CDF', 'Histogram'), loc='upper right')
        plt.xlabel("Gray-Level Intensity")
        plt.ylabel("Frequency")
        output_filename = os.path.basename(output_filename)
        output_filename = os.path.splitext(output_filename)[0]
        plt.savefig(output_filename + "_hist.pdf")
    else:
        raise Exception('ERROR user input of "-s" or "--SHOW_HISTOGRAM".'
                        ' Type "python imhist.py --help" for more information!')

def main():
    parser = argparse.ArgumentParser("This is a command-line tool to generate "
                                     "a histogram from a given PNG file.")
    parser.add_argument("-i", "--INPUT_DATA_PATH", help="path/to/your/input.png", type=str, required=True)
    parser.add_argument("-s", "--SHOW_HISTOGRAM", help="show the histogram (0 for false, 1 for true)", type=int, default=1, required=True)
    parser.add_argument("-o", "--OUTPUT_DATA_PATH", help="output_and_save/the_plot_graph/path", type=str, required=True)
    args = parser.parse_args()
    imhist(args.INPUT_DATA_PATH, args.SHOW_HISTOGRAM, args.OUTPUT_DATA_PATH)

if __name__ == '__main__':
    main()