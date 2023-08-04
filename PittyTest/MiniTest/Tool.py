import os
class Tool:
    def __init__(self, folder_name, SWC_no, filename):
        self.SWC_no = SWC_no
        self.file_name = filename
        self.folder_path =  folder_name
    
    
    
    def join_path(self):
        return os.path.join(self.folder_path, 'BE', 'tools', 'data', 'SWC-' + self.SWC_no, self.file_name + '.json')
        
     
        