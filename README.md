# Convert Images

Repo to convert images to different formats, ideally with multiprocessing

## Convert j2k Images to png

Converts a csv of paths to j2k images to png with multiprocessing

## Usage

Fill in the below with your data

```bash
# Convert images in data.csv in the column file_path to .png outputs in output_folder with 32 threads
python convert_to_png.py \
    --csv_path /path/to/data.csv \
    --column_name file_path \
    --output_folder /path/to/outputs \
    --num_processes 32
```
