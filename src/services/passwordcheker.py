import pythoncom, win32com.client, threading

class PasswordChecker():
    def check_password(self, path, name, password):
        pythoncom.CoInitialize()
        
        xl = win32com.client.DispatchEx('Excel.Application')
        xls_stream = pythoncom.CreateStreamOnHGlobal()   
         
        pythoncom.CoMarshalInterface(xls_stream, 
                                    pythoncom.IID_IDispatch, 
                                    xl._oleobj_, 
                                    pythoncom.MSHCTX_LOCAL, 
                                    pythoncom.MSHLFLAGS_TABLESTRONG) 

        xls_stream.Seek(0,0)
        
        myUnmarshaledInterface = pythoncom.CoUnmarshalInterface(xls_stream, pythoncom.IID_IDispatch)    
        xl = win32com.client.Dispatch(myUnmarshaledInterface)

        try:
            xl_wb = xl.Workbooks.Open('%s\\%s' %(path,name), False, True, None, password)
            if xl_wb.Name:
                xl_wb.Close(False)

                xls_stream.Seek(0,0)
                pythoncom.CoReleaseMarshalData(xls_stream)
                xls_stream = None
                pythoncom.CoUninitialize()

                return password
        except:
            xls_stream.Seek(0,0)
            pythoncom.CoReleaseMarshalData(xls_stream)
            xls_stream = None
            pythoncom.CoUninitialize()
            return None

        xls_stream.Seek(0,0)
        pythoncom.CoReleaseMarshalData(xls_stream)
        xls_stream = None
        pythoncom.CoUninitialize()
        return None
