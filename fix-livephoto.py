import os
import subprocess
import json

def read_exif_data(file_path):
    """Reads EXIF data from the file and returns it as JSON."""
    result = subprocess.run(
        ["exiftool", "-j", file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    if result.returncode != 0:
        raise Exception(f"Error reading EXIF data: {result.stderr}")
    return json.loads(result.stdout)

def get_subsec_datetime_original(file_path):
    """Extracts the SubSecDateTimeOriginal value from the EXIF data."""
    exif_data = read_exif_data(file_path)
    for entry in exif_data:
        if "SubSecDateTimeOriginal" in entry:
            return entry.get("SubSecDateTimeOriginal", None)
    return None

def update_mov_dates(mov_file_path, new_datetime):
    """Updates all date and time entries in the MOV file."""
    try:
        subprocess.run(
            [
                "exiftool",
                "-overwrite_original",
                f"-AllDates={new_datetime}",
                f"-TrackCreateDate={new_datetime}",
                f"-MediaCreateDate={new_datetime}",
                f"-TrackModifyDate={new_datetime}",
                f"-MediaModifyDate={new_datetime}",
                mov_file_path
            ],
            check=True
        )
        print(f"Updated: {mov_file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error updating {mov_file_path}: {e}")

def process_folder(folder_path):
    """Processes the folder, updating .MOV files with corresponding .JPG timestamps."""
    try:
        # Get all files in the folder
        files = os.listdir(folder_path)
        jpg_files = {os.path.splitext(f)[0]: f for f in files if f.lower().endswith('.jpg')}
        mov_files = {os.path.splitext(f)[0]: f for f in files if f.lower().endswith('.mov')}

        # Find matching pairs and update
        for base_name in mov_files.keys():
            if base_name in jpg_files:
                jpg_file_path = os.path.join(folder_path, jpg_files[base_name])
                mov_file_path = os.path.join(folder_path, mov_files[base_name])

                # Get SubSecDateTimeOriginal from JPG
                subsec_datetime = get_subsec_datetime_original(jpg_file_path)
                if subsec_datetime:
                    print(f"Processing: {mov_file_path}")
                    update_mov_dates(mov_file_path, subsec_datetime)
                else:
                    print(f"No SubSecDateTimeOriginal found in {jpg_file_path}. Skipping.")

        print("Processing complete.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Update Dates and Times in .MOV Files in a Folder")

    # Prompt for the folder path
    folder_path = input("Enter the path to the folder: ").strip()

    if not os.path.isdir(folder_path):
        print("The provided path is not a valid directory.")
        return

    process_folder(folder_path)

if __name__ == "__main__":
    main()