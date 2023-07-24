import cv2
import numpy as np
import argparse

# AnnotationTool.py -- The tool that can create binary mask after annotation

# Global variables
drawing = False
polygon_points = []


def draw_polygon(event, x, y, flags, param):
    global drawing, polygon_points

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        polygon_points = [(x, y)]

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.polylines(image, [np.array(polygon_points)], isClosed=True, color=(255, 255, 255), thickness=2)
        cv2.fillPoly(mask, [np.array(polygon_points)], (255, 255, 255))
        polygon_points = []

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(image, polygon_points[-1], (x, y), (255, 255, 255), 2)
            polygon_points.append((x, y))

def AnnotationTool(input_filename) -> None:
    if not(input_filename.lower().endswith('.png')):
        raise Exception("Please provide a filename with a .png extension for the input file.")

    global image, mask

    image = cv2.imread(input_filename, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise Exception("Error: No such file or directory")

    mask = np.zeros_like(image)
    cv2.namedWindow('Annotation Tool')
    cv2.setMouseCallback('Annotation Tool', draw_polygon)

    while True:
        cv2.imshow('Annotation Tool', image)
        key = cv2.waitKey(1)

        if key == ord('c'):
            image = cv2.imread(input_filename, cv2.IMREAD_GRAYSCALE)
            mask.fill(0)

        elif key == ord('s'):
            cv2.imwrite(input_filename + '_binary_mask.png', mask)
            break

        elif key == 27:  # ESC key to exit
            break

    cv2.destroyAllWindows()

def main() -> None:
    parser = argparse.ArgumentParser(description="This is a tool for image segmentation annotation, "
                                                 "but you need to provide the path to the "
                                                 "input image using the command line.")
    parser.add_argument("-i", "--INPUT_DATA_PATH", help="path/to/your/input.dcm", type=str, required=True)
    args = parser.parse_args()
    AnnotationTool(args.INPUT_DATA_PATH)


if __name__ == '__main__':
    main()