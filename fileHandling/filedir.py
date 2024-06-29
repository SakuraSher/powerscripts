import os
import shutil
import datetime

def backup_files(source_dir,backup_dir):
    cur_dir = os.getcwd()
    cur_folder = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.abspath(os.path.join(cur_folder,source_dir))
    bpath = os.path.abspath(os.path.join(cur_folder,backup_dir))
    print(fpath)

    listoffiles = os.listdir(fpath)
#    if not os.path.exists(backup_dir):
#        os.mkdir(backup_dir)

    current_date = datetime.datetime.now().strftime('%d-%m-%Y')
    backup_path = os.path.join(backup_dir)

    for filename in os.listdir(fpath):
        source_file = os.path.join(fpath,filename)
        destination_file = os.path.join(bpath,filename)
        shutil.copy2(source_file,destination_file)
        print(f"Backing up{source_file} to {destination_file}")


if __name__ == "__main__":
   
    backup_files("source","backup")

   