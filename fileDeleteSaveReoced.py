import logging
import time
import os

# first we created log file to stored recored

#logging.basicConfig(filename='delete_file_record.log',level=logging.INFO)
f=open("Gajanan.txt",'a')
f.close()
directory="C:\\Users\\Admin\\practice_folder"
print(directory)

# second set  number of day to keep this file before deleting
keep_day=1

# then set the number of day to wait berfore deleting empty folder
wait_day=7
# take current time
current_time=time.time()

# to reach each file in folder use for loop
for root,dirs,files in os.walk(directory,topdown=False):
    for file in files:
        file_paath=os.path.join(root,file)
        print(os.path.getmtime(file_paath))
        # to check file is older than number of day to keep
        if(current_time - os.path.getmtime(file_paath)) // (24*3600)> keep_day:
            os.remove(file_paath)
            f=open("Gajanan.txt",'a')
            f.write("Delete file :{}".format(file_paath))
            f.close()
            #logging.info("Delete file :{}".format(file_paath))
    for dir in dirs:
        dir_path=os.path.join(root,dir)
        # check directory is empty or not
        if not os.listdir(dir_path):

            # check dir is older than number of day to keep
            if(current_time - os.path.getmtime(dir_path)) // (24 * 3600)> wait_day:
                os.rmdir(dir_path)
                logging.info("deleted empty directory {} :".format(dir_path))
