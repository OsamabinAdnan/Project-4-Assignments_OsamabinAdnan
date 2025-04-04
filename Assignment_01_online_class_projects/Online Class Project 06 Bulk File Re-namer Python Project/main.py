import os

def main():
    # Initialize counter for new filenames
    i = 0
    # Define the directory path where images are stored
    path = "images/"
    
    # Iterate through each file in the specified directory
    for filenme in os.listdir(path):
        # Create new filename with counter number
        my_dest = "imges" + str(i) + ".jpg"
        # Construct full source path
        my_source = path + filenme
        # Construct full destination path
        my_dest = path + my_dest
        # Rename the file
        os.rename(my_source, my_dest)
        # Increment counter for next filename
        i += 1

# Execute main function only if script is run directly
if __name__ == '__main__':
    main()