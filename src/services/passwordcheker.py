import pythoncom, win32com.client, threading

class PasswordChecker():
    xls_stream = None

    def __init__(self):
        pythoncom.CoInitialize()
        xl = win32com.client.DispatchEx('Excel.Application')
        self.xls_stream = pythoncom.CreateStreamOnHGlobal()   
         
        pythoncom.CoMarshalInterface(self.xls_stream, 
                                    pythoncom.IID_IDispatch, 
                                    xl._oleobj_, 
                                    pythoncom.MSHCTX_LOCAL, 
                                    pythoncom.MSHLFLAGS_TABLESTRONG) 

        xl = None

    def __del__(self):
        self.xls_stream.Seek(0,0)
        pythoncom.CoReleaseMarshalData(self.xls_stream)
        self.xls_stream = None
        pythoncom.CoUninitialize()

    def check_password(self, path, name, password):
        pythoncom.CoInitialize()

        self.xls_stream.Seek(0,0)
        
        myUnmarshaledInterface = pythoncom.CoUnmarshalInterface(self.xls_stream, pythoncom.IID_IDispatch)    
        xl = win32com.client.Dispatch(myUnmarshaledInterface)

        try:
            xl_wb = xl.Workbooks.Open('%s\\%s' %(path,name), False, True, None, password)
            if xl_wb.Name:
                xl_wb.Close(False)
                return True
        except:
            return False

        return False
