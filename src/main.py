from services.passgen import PassGenerator
from services.repo import FileRepository
from services.passwordcheker import PasswordChecker

import concurrent.futures
import string


xls_path = 'C:\\@Work\\P\\GitHub\\bruteforce\\src\\xlsx'
xls_name = 'test.xlsx'

pass_service = PassGenerator(string.ascii_letters+string.punctuation+'0123456789')
file_service = FileRepository('C:\\@Work\\P\\GitHub\\bruteforce\\src\\data')
chek_service = PasswordChecker()

def executie(p):
    return chek_service.check_password(xls_path,xls_name,p)

cmd_gen_pass = False
cmd_try_pass = True
cmd_pass_size = 3
cmd_thread_number = 1

if cmd_gen_pass:
    file_service.remove_all_files()
    generated_passwords = pass_service.get_all(cmd_pass_size)
    for new_pass in generated_passwords:
        file_service.add_password(('%d.txt' %(cmd_pass_size)), new_pass)

if cmd_try_pass:
    loaded_pass = list(file_service.load_file(('%d.txt' %(cmd_pass_size))))
    for page in range(0,len(loaded_pass),cmd_thread_number):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for p in loaded_pass[page:page+cmd_thread_number]:
                futures.append(executor.submit(executie,p))

            for f in concurrent.futures.as_completed(futures):
                print(f.result())
 
print('Terminat')