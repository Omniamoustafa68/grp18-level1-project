# 5.Task: program to move file from dir to another
import os
import shutil
source_file = 'C:\\movefile\\people_filter.csv'
destination_file = 'C:\\movefile\\New folder\\people_filter.csv'
shutil.move(source_file, destination_file)