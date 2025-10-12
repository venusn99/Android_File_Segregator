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
            nested_obj=Dextractor.FolderAction(src_dir=self._src_dir, dst_dir=self._dst_dir, action =self.action ,format=self.subfolder_format_number).create_nested_directory()


# modify the below config with your values
config = {'src_dir': '/home/venu/python-sandbox/playground/folder1', 'dst_dir' : '/home/venu/python-sandbox/playground/dst_folder', 'action':'move', 'subfolder_format_number': 2 }

workflow1 = segregate_android_files(**config)
print(workflow1.workflow())