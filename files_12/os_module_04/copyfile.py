#3.Task: Copy a file from one location to another
import os
import shutil
source_file = 'C:\\copyfile\\omnia.csv'
destination_file ='C:\\copyfile\\New folder\\omnia.csv'
shutil.copyfile(source_file, destination_file)