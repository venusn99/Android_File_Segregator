import core.Dextractor as Dextractor
import argparse


class segregate_android_files():
    def __init__(self, **values):
        self._src_dir = values['src_dir']
        self._dst_dir = values['dst_dir']
        self.action = values['action']
        self.subfolder_format_number = values['subfolder_format_number']
        self.unattend_files = values['unattend_files']
    def get_input_values(self):
        print(f'The source directory is {self._src_dir}\n')
        print(f'The destination directory is {self._dst_dir}\n')
        print(f'The File action is {self.action}\n')
    def workflow(self):
        path1 = Dextractor.FilePathCheck(self._src_dir)
        path2 = Dextractor.FilePathCheck(self._dst_dir)
        if path1.path_exists_check() and path2.path_exists_check():
            # below will create nested directories where ever the files are present at source directory
            nested_obj=Dextractor.FolderAction(src_dir=self._src_dir, dst_dir=self._dst_dir, action =self.action.lower() ,format=self.subfolder_format_number, unattend_files=self.unattend_files).create_nested_directory()


if __name__ == "__main__":
    # src_dir : str = input("Enter the source directory: ")
    # dst_dir : str = input("Enter the destination directory: ")
    # action : str = input("Enter the action (copy/move): ")
    # unattend_files : bool = input("Handle the unattended files? (True/False): ")
    # subfolder_format_number : int = int(input("Enter the subfolder format number: \n\t1: YYYY \n\t2: YYYY/MM \n\t3: YYYY/MM/DD \n"))
    # config = {'src_dir': src_dir, 'dst_dir': dst_dir, 'action': action, 'subfolder_format_number': subfolder_format_number, 'unattend_files': unattend_files}
    parser = argparse.ArgumentParser(description="Segregate Android files into organized folders.")
    parser.add_argument("--src_dir", "-S", required=True, help="Source directory")
    parser.add_argument("--dst_dir", "-D", required=True, help="Destination directory")
    parser.add_argument("--action", "-A", choices=["copy", "move"], required=True, help="Action to perform on files")
    parser.add_argument("--unattend_files", "-U", choices=["True", "False"], help="Handle unattended files")
    parser.add_argument("--subfolder_format_number", "-F", type=int, choices=[1, 2, 3], required=True, help="Subfolder format number")
    args = parser.parse_args()
    workflow1 = segregate_android_files(**vars(args))
    print(vars(args))
    # workflow1.workflow()
