import os
import argparse

def rename_png_files(input_directory):
    if not os.path.exists(input_directory):
        print(f"Error: Directory '{input_directory}' does not exist.")
        return

    if not os.path.isdir(input_directory):
        print(f"Error: '{input_directory}' is not a directory.")
        return

    files = os.listdir(input_directory)
    png_files = [file for file in files if file.lower().endswith('.png')]

    if not png_files:
        print("No PNG files found in the directory.")
        return

    png_files.sort()

    for i, filename in enumerate(png_files):
        new_filename = f"{i}.png"
        source_path = os.path.join(input_directory, filename)
        destination_path = os.path.join(input_directory, new_filename)

        try:
            os.rename(source_path, destination_path)
            print(f"Renamed '{filename}' to '{new_filename}'")
        except Exception as e:
            print(f"Error renaming '{filename}': {str(e)}")

def main() -> None:
    parser = argparse.ArgumentParser(description="This is a command-line tool which can"
                                                 " renames PNG files in a specific directory.")
    parser.add_argument("-i", "--input_directory", type=str, help="the directory to rename PNG files", required=True)
    args = parser.parse_args()
    rename_png_files(args.input_directory)
if __name__ == "__main__":
    main()
