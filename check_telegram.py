from smsactivate.api import SMSActivateAPI

from settings.settings import TOKEN

class CheckTelegram:
    def __init__(self):
        self.smsa_core = SMSActivateAPI(TOKEN)

    def get_countries(self):
        countries = self.smsa_core.getCountries()
        print(f'{countries}')

if __name__ == '__main__':
    core_sms_check = CheckTelegram()
    response = core_sms_check.get_countries()

    print(response)
