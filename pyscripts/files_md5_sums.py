## Purpose: Program to generate a file listing the md5 checksums of the files in the
## current directory and any sub-directories (if present)
## Python version written for: 3.7.3
## Pre-requisites: None
## Inputs: Current working directory

# Imports
import os
import os.path
import hashlib

# Function to return a list of files starting in the current directory the script is invoked in
def obtain_files():
    cwd = os.path.normpath(os.getcwd())
    return [os.path.join(cwd, f) for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd,f))]

# Function to generate a list of files and their md5 hashes (future TODO: Use different hash algorithms)
def obtain_hashes():
    files = obtain_files()
    list_o_hashes = []
    for elem in files:
        md5_hash = hashlib.md5()
        with open(elem, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                md5_hash.update(chunk)
        list_o_hashes.append("Filename: {},md5 Hash: {}\n".format(elem,md5_hash.hexdigest()))
    return list_o_hashes

# Function to create the hash file
def create_list_hash_file():
    results = obtain_hashes()
    with open('files_list_with_md5s.txt', 'w') as f:
        for md5_elem in results:
            f.write(md5_elem)

if __name__=="__main__":
    create_list_hash_file()
