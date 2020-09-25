import win32com.client

class PasswordChecker:
    xl_app = win32com.client.Dispatch('Excel.Application')
    
    def check_password(self, path, name, password):
        try:
            xl_wb = self.xl_app.Workbooks.Open('%s\\%s' %(path,name), False, True, None, password)
            if xl_wb.Name:
                xl_wb.Close(False)
                return True
        except:
            return False      

    