import os


class FileInfo:
    def __init__(self, path):
        self.original_path = path
        self.file_name = os.path.basename(path)

    def get_info(self):
        return (
            self.file_name,
            self.original_path,
            os.path.abspath(self.file_name),
            os.path.getsize(self.file_name)
        )
