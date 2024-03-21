import os
import argparse
from PIL import Image
import pandas as pd
from multiprocessing import Pool, cpu_count

def parse_args():
    parser = argparse.ArgumentParser(description="Convert files from CSV to PNG.")
    parser.add_argument("--csv_path", type=str, help="Path to the CSV file")
    parser.add_argument("--column_name", type=str, help="Name of the column containing file names in the CSV")
    parser.add_argument("--output_folder", type=str, help="Output folder for PNG files")
    parser.add_argument("--num_processes", type=int, help="Number of CPU threads to process")
    return parser.parse_args()


def convert_file(file_path, output_folder):
    try:
        if '.j2k' in file_path:
            image = Image.open(os.path.join(os.getcwd(), file_path))
            output_path = os.path.join(output_folder, os.path.splitext(os.path.basename(file_path))[0] + ".png")
            print(output_path)
            # image.save(output_path)
    except Exception as e:
        print(f"Error for {file_path}: {e}")


def main():
    args = parse_args()

    df = pd.read_csv(args.csv_path)
    file_names = df[args.column_name].tolist()
    output_folder = args.output_folder
    num_processes = args.num_processes

    # Using multiprocessing pool to process images concurrently
    with Pool(num_processes) as pool:
        pool.starmap(convert_file, [(file_name, output_folder) for file_name in file_names])


if __name__ == "__main__":
    main()
