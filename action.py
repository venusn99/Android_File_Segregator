import core.Dextractor as Dextractor
import os
class segregate_android_files():
    def __init__(self, **values):
        self._src_dir = values['src_dir']
        self._dst_dir = values['dst_dir']
        self.action = values['action']
        self.subfolder_format_number = values['subfolder_format_number']
    def get_input_values(self):
        print(f'The source directory is {self._src_dir}\n')
        print(f'The destination directory is {self._dst_dir}\n')
        print(f'The File action is {self.action}\n')
    def workflow(self):
        path1 = Dextractor.FilePathCheck(self._src_dir)
        path2 = Dextractor.FilePathCheck(self._dst_dir)
        if path1.path_exists_check() and path2.path_exists_check():
            # below will create nested directories where ever the files are present at source directory
            nested_obj=Dextractor.FolderAction(src_dir=self._src_dir, dst_dir=self._dst_dir, action =self.action.lower() ,format=self.subfolder_format_number).create_nested_directory()


if __name__ == "__main__":
    src_dir = input("Enter the source directory: ")
    dst_dir = input("Enter the destination directory: ")
    action = input("Enter the action (copy/move): ")
    subfolder_format_number = int(input("Enter the subfolder format number: \n\t1: YYYY \n\t2: YYYY/MM \n\t3: YYYY/MM/DD \n"))
    config = {'src_dir': src_dir, 'dst_dir': dst_dir, 'action': action, 'subfolder_format_number': subfolder_format_number}

    workflow1 = segregate_android_files(**config)
    workflow1.workflow()