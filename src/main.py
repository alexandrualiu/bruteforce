from services.passgen import PassGenerator
from services.repo import FileRepository
from services.passwordcheker import PasswordChecker
from conf.config import Settings 
from clients import Client

pass_service = PassGenerator(Settings.pass_generator_pattern)
file_service = FileRepository(Settings.data_folder)
chek_service = PasswordChecker()

client = Client(file_service,pass_service,chek_service)

client.load()

client.execute()