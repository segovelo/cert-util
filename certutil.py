#!/usr/bin/env python3
from argparse import ArgumentParser
import subprocess
import os
import sys
import glob

download_folder = "<YOUR_LOCAL_PATH>\\Downloads"
if len(sys.argv) > 1:
    file_name = sys.argv[1]
    full_path_file = os.path.join(download_folder, file_name)
else:
    list_of_files = glob.glob(f"{download_folder}\\*.exe")
    if len(list_of_files):
        full_path_file = max(list_of_files, key=os.path.getctime) 
        file_name = full_path_file.split("\\")[-1]
        print(f"The most recent *.exe file {full_path_file}")
    else:
        print("*.exe file not found in Downloads folder.") 
list_of_checksum = glob.glob(f"{download_folder}\\*.sha256") 
list_of_checksum.extend(glob.glob(f"{download_folder}\\*.sha512")) 
list_of_checksum.extend(glob.glob (f"{download_folder}\\*.sha1")) 
list_of_checksum.extend(glob.glob(f"{download_folder}\\*.md5")) 
if len(list_of_checksum) > 0:
    if len(sys.argv) > 1:
        for f in list_of_checksum: 
            if file_name in f:
                checksum_file = f
                break
    else:
        checksum_file = max(list_of_checksum, key=os.path.getctime) 
    checksum_ext = checksum_file.split(".")[-1] 
    if f"{full_path_file}.{checksum_ext}" == checksum_file:
        try:
            my_file = open(f"{checksum_file}", "r", encoding="utf-8") 
        except IOError:
            print("Unable to find file")
checksum = ""
try:
    checksum = my_file.read()
except UnicodeDecodeError:
    print("UnicodeDecodeError: 'charmap' codec can't decode byte")
finally:
    my_file.close()
result = subprocess.Popen((f"certutil -hashfile {full_path_file} {checksum_ext}"),stdout=subprocess.PIPE).stdout
lines = result.readlines()
l = lines[1][:-2].decode("utf-8")
for line in lines:
    print(line[:-2].decode("utf-8"))
if l == checksum:
    print(f"{file_name} file is OK :)")
else:
    print(f"{file_name} is corrupted!") 
result.close()