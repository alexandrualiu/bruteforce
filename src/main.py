from services.passgen import PassGenerator
from services.repo import FileRepository
from services.passwordcheker import PasswordChecker

import string

xls_path = 'C:\\Users\\alexa\\Documents\\Data\\Work\\BruteForce\\xlsx'
xls_name = 'test.xlsx'

pass_service = PassGenerator(string.ascii_letters+string.punctuation+'0123456789')
file_service = FileRepository('C:\\Users\\alexa\\Documents\\Data\\Work\\BruteForce\\data')
chek_service = PasswordChecker()

cmd_gen_pass = False
cmd_try_pass = True
cmd_pass_size = 3

if cmd_gen_pass:
    file_service.remove_all_files()
    generated_passwords = pass_service.get_all(cmd_pass_size)
    for new_pass in generated_passwords:
        file_service.add_password(('%d.txt' %(cmd_pass_size)), new_pass)

if cmd_try_pass:
    loaded_pass = file_service.load_file(('%d.txt' %(cmd_pass_size)))
    for item in loaded_pass:
        result = chek_service.check_password(xls_path, xls_name, item)
        if result:
            print (item)
            break

print('Terminat')