# LivePhoto DateTime Fix

This script fixes inconsistencies between the date and time metadata of iPhone Live Photos by aligning the `.MOV` metadata with the corresponding `.JPG` metadata. The script writes the date/time information from the `.JPG` file to the `.MOV` file.

## Prerequisites

1. **Check Python and Pip Versions**  
Ensure you have Python 3 and pip installed. Verify their versions with the following commands:  
`python3 --version`  
`pip3 --version`  
If Python 3 or pip is not installed, refer to the [Python installation guide](https://www.python.org/downloads/).

2. **Install ExifTool**  
ExifTool is a powerful tool for reading and writing metadata. Install it using Homebrew (macOS):  
`brew install exiftool`  
Verify the installation:  
`exiftool -ver`  
For other operating systems, follow the official [ExifTool installation instructions](https://exiftool.org/).

3. **Set Up a Virtual Environment (optional)**  
Create a virtual environment to isolate your dependencies:  
`python3 -m venv exiftool_env`  
`source exiftool_env/bin/activate`  
To deactivate the virtual environment later, run:  
`deactivate`

4. **Install PyExifTool**  
Install the required Python package `pyexiftool` for interacting with ExifTool:  
`pip3 install pyexiftool`

5. **Run the Script**  
Execute the script to fix the metadata:  
`python3 fix-livephoto.py`


## Example Directory Structure

Ensure that the `.JPG` and `.MOV` files are in the same directory and named consistently. Example:  
`/path/to/livephotos/`  
`  - IMG_1234.JPG`  
`  - IMG_1234.MOV`  
The script will automatically pair the `.JPG` and `.MOV` files based on their filenames.


## Additional Notes

- The script only modifies metadata and does not affect the actual photo or video content.
- Create backups of your files before running the script, as metadata changes are irreversible.


## Contributing

Contributions, issues, and feature requests are welcome!
