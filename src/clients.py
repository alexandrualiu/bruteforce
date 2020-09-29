from conf.config import Settings
import concurrent.futures
import sys

class Client:
    def __init__(self, fileservice,generationservice,checkservice):
        self.xls_name = None
        self.cmd_gen_pass = False
        self.cmd_try_pass = False
        self.cmd_pass_size = None
        self.cmd_thread_number = 1
        self.svc_files = fileservice
        self.svc_generator = generationservice
        self.svc_checker = checkservice

    def print_help(self):
        help_text = """This is an experimental programm and it is not meant to do any harm 
        Please remember that accessing data you don't own it's illegal and you can go to jail

        CLI Syntax
        python main.py [param_name=param_value,]

        Parameters:
        \txls_name
        \t\texcel filename that exists in XLSX folder
        \tcmd_gen_pass
        \t\tif this is 'true' the program will generate password
        \tcmd_try_pass
        \t\tif this is 'true' the program will read the passwords from the file and will try to open the XLSX file
        \tcmd_pass_size
        \t\tthis is integer that will specify what password length should be used (if you use long numbers here will take decades to generate all of them)
        \tcmd_thread_number
        \t\ta number that secifies how many passwords will be trid at oance

        Usage:
        To generate passwords you should pass: cmd_gen_pass=true cmd_pass_size=[what length you want]

        Example:
        python main.py cmd_gen_pass=true cmd_pass_size=2
        
        To try passwords: You should pass xls_name="" cmd_try_pass=true cmd_pass_size=[what length you want] cmd_thread_number=[how many threads you want]
        
        Example:
        python main.py xls_name="test.xlsx" cmd_try_pass=true cmd_pass_size=2 cmd_thread_number=10
        """
        print(help_text)

    def load(self):
        self.print_help()
        for arg in sys.argv:
            arg_pair = arg.split('=')
            if len(arg_pair) == 2:
                if arg_pair[0] == 'xls_name':
                    self.xls_name = arg_pair[1]

                if arg_pair[0] == 'cmd_gen_pass':
                    if (arg_pair[1].lower() == "true") or arg_pair[1] == "1":
                        self.cmd_gen_pass = True
                    elif  (arg_pair[1].lower() == "false") or arg_pair[1] == "0":
                        self.cmd_gen_pass = False
                    else:
                        self.cmd_gen_pass = False

                if arg_pair[0] == 'cmd_try_pass':
                    if (arg_pair[1].lower() == "true") or arg_pair[1] == "1":
                        self.cmd_try_pass = True
                    elif  (arg_pair[1].lower() == "false") or arg_pair[1] == "0":
                        self.cmd_try_pass = False
                    else:
                        self.cmd_try_pass = False

                if arg_pair[0] == 'cmd_pass_size':
                    self.cmd_pass_size = int(arg_pair[1])

                if arg_pair[0] == 'cmd_thread_number':
                    self.cmd_thread_number = int(arg_pair[1])
    
    def execute(self):
        # generate passwords
        if self.cmd_gen_pass:
            generated_passwords = self.svc_generator.get_all(self.cmd_pass_size)
            passwords_file_name = '%d.txt' %(self.cmd_pass_size)
            self.svc_files.remove_files([passwords_file_name])
            for new_pass in generated_passwords:
                self.svc_files.add_password(passwords_file_name, new_pass)
        
        # test passwords
        # it works on diff threads, but Excel can't open the same workbook in the same app
        if self.cmd_try_pass:
            break_it = None
            loaded_pass = list(self.svc_files.load_file(('%d.txt' %(self.cmd_pass_size))))
            for page in range(0,len(loaded_pass),self.cmd_thread_number):
                break_it = False
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    futures = []
                    for p in loaded_pass[page:page+self.cmd_thread_number]:
                        futures.append(executor.submit(self.svc_checker.check_password, path=Settings.xls_folder, name=self.xls_name, password=p))

                    for f in concurrent.futures.as_completed(futures):
                        correct_pass = f.result()
                        if not correct_pass is None:
                            print('The correct password is: %s' %(correct_pass))
                            break_it = True
                            break
                
                if break_it:
                    break
            
            if not break_it:
                print("Password was not found")

            