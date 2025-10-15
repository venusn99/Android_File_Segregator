import shutil
import os
class FileTransporter():
    def __init__(self, src_file, dst_file, action='copy'):
        self.src_file = src_file # takes full path
        self.dst_file = dst_file # takes full path, you need to provide the filename to be copied as 
        self.action=action
        os.makedirs(os.path.dirname(self.dst_file), exist_ok=True) # create destination directory if not exists, Triggeres during exception cause for unattended_files
        if self.action == 'copy':
            self.copy_with_attributes()
        elif self.action == 'move':
            self.move_the_file()
        else:
            raise ValueError (f'The action is not supported, only copy or move is supported\n')

    def copy_with_attributes(self):
        print('copying')
        shutil.copy2(src=self.src_file,dst=self.dst_file)
    def move_the_file(self):
        print('moving')
        shutil.move(src=self.src_file,dst=self.dst_file)