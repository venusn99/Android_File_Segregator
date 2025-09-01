import os
import re
from pathlib import Path
import shutil
# class File_syntax_exampler():
#     # def __init__():
#     #     return os.path.dirname(os.path.realpath(__file__))

class FilePathCheck(): # Class to validate if file path is valid
    '''
    This class validates whether the source and destination directory exists in the system,

    Args:
        source_directory: takes the string of source path (tested in linux)
        destination_directory: takes the string of destination path (tested in linux)
    Return:
        'True' if both source and destinations args are valid else 'False'
    '''
    def __init__(self, source_directory, destionation_directory):
        self.src_dir=source_directory
        self.dst_dir=destionation_directory
        self.path_exists_check()
    def path_exists_check(self):
        src_exists= os.path.exists(self.src_dir)
        dst_exists = os.path.exists(self.dst_dir)
        return src_exists and dst_exists

class ExtractFileInfo():
    '''
        Extracts the File's Year , Month and Day from Android's system fileformed name. extracted using regular expression.

    Args: Requires the file with absolute path.
    Return:
            IF valid : returns Year, Month and Day
            else : ValueError
    '''
    def __init__(self, file):
        self.file=file
        self.year , self.month, self.day = self.split_filename()
    def extract_basename(self):
        # extracts the basename of the file ex: /home/user1/file1.jpg the functions extracts file1.jpg
        print("extracting the filename from relative path\n")
        return os.path.basename(self.file)
    def split_filename(self):
        basename=self.extract_basename()
        pattern = r"([\d]{8})" # matches 8 digit pattern in filename. in  IMG_20251618_0813.JPG matches "20251618"
        match = re.search(pattern, basename)
        if match is not None:
            return match.group(0)[:4], match.group(0)[4:6],match.group(0)[6:8]
        else:
            raise ValueError ( f"{self.file} doesn't have YYYYMMDD format to extract:  Pattern not matching\n")
    def extract_date_parts(self):
        return self.year, self.month, self.day
class FileAction():
    def __init__(self,src_dir,dst_dir,action='copy', format=None ):
        self.src_path=src_dir
        self.dst_path=dst_dir
        self.action=action
        self.format = format
        if FilePathCheck(self.src_path,self.dst_path):
            print(" Source and Destination directory is valid\n")
            print("Creating nested dircetory")
            self.create_nested_directory()
        else:
            print("Source or Destination Directory is invalid ")
    def create_nested_directory(self):
        """
        Replicates the directory structure of the source inside the destination.

        Args:
            source (str): The source directory whose structure needs to be replicated.
            destination (str): The destination directory where the structure will be created.

        Returns:
            None
        """
        try:
            print("in the function")
            for root, dirs, files in os.walk(self.src_path):
                print(root, files)
                relative_path = os.path.relpath(root, self.src_path)
                print(files)
                if len(files) > 0:
                    for file in files:
                        file_path = os.path.join(root, file)
                        file_info = ExtractFileInfo(file_path)
                        self.year, self.month, self.day = file_info.extract_date_parts()
                    #Create corresponding directory in destination
                        if self.format == 1:
                            destination_path = os.path.join(self.dst_path, relative_path, self.year)
                        elif self.format == 2:
                            destination_path = os.path.join(self.dst_path, relative_path, self.year, self.month)
                        elif self.format == 3:
                            destination_path = os.path.join(self.dst_path, relative_path, self.year, self.month, self.day)
                        else:
                            destination_path = os.path.join(self.dst_path, relative_path)
                        os.makedirs(destination_path,exist_ok=True)
                        print(f"Created: {destination_path}")
        except Exception as e:
            print(f"An error occured: {e}")