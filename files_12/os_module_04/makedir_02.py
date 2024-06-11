# 2. Task: Create a new directory if it does not exist
import os
if not os.path.exists('C:\\my_file\\new_folder'):
    os.makedirs('C:\\my_file\\new_folder')
