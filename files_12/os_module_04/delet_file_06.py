# 6.Task Delete a file if it exists
import os
from send2trash import send2trash
file_to_delet = 'C:\\delet_file\\people_delete.csv'
if os.path.exists(file_to_delet):
    os.remove(file_to_delet)      #delete without recyclepin

file_delet = 'C:\\delet_file_recyclepin\\people_remove.csv'
send2trash(file_delet) #put on recyclepin