# Bulk Image File Renamer

A simple Python script that automatically renames image files in a directory with sequential numbered names.

## Description

This script renames all files in an `images/` directory to follow the format `imgesX.jpg` where X is a sequential number starting from 0. For example: `imges0.jpg`, `imges1.jpg`, `imges2.jpg`, etc.

## Requirements

- Python 3.x
- A directory named `images` in the same location as the script
- Read/write permissions for the images directory

## Usage

1. Place your image files in the `images/` directory
2. Run the script:
```sh
python main.py
```

## How It Works

The script performs the following operations:
1. Initializes a counter starting at 0
2. Scans the `images/` directory
3. For each file found:
   - Creates a new filename in the format `imgesX.jpg`
   - Renames the original file to the new format
   - Increments the counter

## File Structure

```
project/
│   main.py
│   README.md
└───images/
    │   imges0.jpg
    │   imges1.jpg
    │   imges2.jpg
    │   ...
```

## Warning

- Make sure to backup your files before running the script
- All files in the images directory will be renamed regardless of their original names