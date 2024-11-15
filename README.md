# Image Resizing Tool

This is a Python-based tool that resizes an image by a specified percentage and saves the resized image as a new file. The project uses the OpenCV library for image processing.

## Project Overview

The tool reads an image from a source file, resizes it based on a configurable scale percentage, and saves the resized image to a destination file.

## Prerequisites

1. **Python 3.6 or higher**: Make sure you have Python installed on your system.
2. **OpenCV library**: This library is required for image processing.

## Setting Up the Project

### 1. Clone the Repository (optional)

If you have the code in a repository, you can clone it. Otherwise, download the code directly.

```bash
git clone <repository-url>
```

### 2. Install Required Libraries

Open a terminal, navigate to the project directory, and install the required libraries with:

```bash
pip install opencv-python
```

### 3. Add Your Source Image

Place the image you want to resize in the project directory and name it accordingly. 

Then modify the `source` variable in the code to specify a different image filename.

```python
source = Your_File_Name
```

Then modify the `destination` variable in the code to specify the output image filename.

```py
destination = Output_File_Name
```

### 4. Run the Application

To run the image resizing tool, use:

```bash
python main.py
```

## Customization
- Changing the Scale Percentage: Adjust the `scale_percent` variable to control the resize percentage.

- Changing Source/Destination Filenames: Modify the `source` and `destination` variables to specify different input and output filenames.

## Usage
1. The script will read the image from the source path (default is `Ghost.jpg`).

2. It resizes the image to the specified scale percentage (default is 50%).

3. The resized image is saved to the destination path (default is `newGhost.jpg`).