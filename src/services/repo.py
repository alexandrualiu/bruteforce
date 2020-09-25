import os
class FileRepository:
    def __init__(self, path):
        self.data_folder = path
    
    def add_password(self, filename, password):
        file = open(('%s\\%s' %(self.data_folder, filename)),'a')
        file.write(password+"\n")
        file.close()

    def load_file(self, filename):
        ret = set()
        file = open(('%s\\%s' %(self.data_folder, filename)),'rt')
        for line in file:
            ret.add(line.replace('\n',''))
        
        return ret

    def remove_files(self, file_names):
        for file_name in file_names:
            os.remove(('%s\\%s' %(self.data_folder, file_name)))
    
    def remove_all_files(self):
        for file_name in os.listdir(self.data_folder):
            os.remove(('%s\\%s' %(self.data_folder, file_name)))