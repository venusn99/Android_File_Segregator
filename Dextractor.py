import os
# class File_syntax_exampler():
#     # def __init__():
#     #     return os.path.dirname(os.path.realpath(__file__))

class DirSyntax():
    def __str__(self):
        return  os.path.dirname(os.path.realpath(__file__))
class FileSourceDir():
    def get_source_directory(self):
        return input(f"Enter the source directory where the files should be copy/move from\n hint: directory format should be like \"{DirSyntax()}\" ")
class FileDestinationDirectory():
    def set_destination_directoy(self):
        return input(f"Enter the destination directory where the files should be copy/move to\n hint: directory format should be like \"{DirSyntax()}\" ")
class FileOperation():
    def __init__(self, source_directory, destionation_directory,action='copy',):
        self.action_type=action.lower()
        self.src_dir=source_directory
        self.dst_dir=destionation_directory
        print(f"the source directory is {self.src_dir}")
    def path_exists_check(self):
        src_exists= os.path.exists(self.src_dir)
        dst_exists = os.path.exists(self.dst_dir)
        return src_exists and dst_exists
    def action(self):
        if self.path_exists_check():
            print("The path is valid")
        else:
            print("the source path is invalid please check\n")



src_d = FileSourceDir()
src_path= src_d.get_source_directory()
dst_d = FileDestinationDirectory()
dst_path= dst_d.set_destination_directoy()


file1 = FileOperation(src_path,dst_path)
file1.action()

