import os
import re
# class File_syntax_exampler():
#     # def __init__():
#     #     return os.path.dirname(os.path.realpath(__file__))

class DirSyntax(): # a class to get the syntax of directory for OS
    def __str__(self):
        return  os.path.dirname(os.path.realpath(__file__))
class FileSourceDir(): # Get the Source Directory
    def get_source_directory(self):
        return input(f"Enter the source directory where the files should be copy/move from\n hint: directory format should be like \"{DirSyntax()}\" ")
class FileDestinationDirectory(): # Get the destination Directory
    def set_destination_directoy(self):
        return input(f"Enter the destination directory where the files should be copy/move to\n hint: directory format should be like \"{DirSyntax()}\" ")
    
class FileValidCheck(): # Class to validate if file path is valid
    def __init__(self, source_directory, destionation_directory):
        self.src_dir=source_directory
        self.dst_dir=destionation_directory
        self.path_exists_check()
    def path_exists_check(self):
        src_exists= os.path.exists(self.src_dir)
        dst_exists = os.path.exists(self.dst_dir)
        return src_exists and dst_exists

class ExtractFileInfo():
    def __init__(self, file):
        self.file=file
    def extract_basename(self):
        print("extracting the filename from relative path\n")
        return os.path.basename(self.file)
    def split_filename(self):
        basename=self.extract_basename()
        pattern = r"([\d]{8})"
        match = re.search(pattern, basename)
        if match is not None:
            return match.group(0)[:4], match.group(0)[4:6],match.group(0)[6:8]
        else:
            return f"{self.file} doesn't have YYYYMMDD format to extract:  Patten not matching\n"


if __name__ == "__main__":
    print("This will only execute when module.py is run directly!")
    src_d = FileSourceDir()
    src_path= src_d.get_source_directory()
    dst_d = FileDestinationDirectory()
    dst_path= dst_d.set_destination_directoy()
    file1 = FileValidCheck(src_path,dst_path)
    file1.action()