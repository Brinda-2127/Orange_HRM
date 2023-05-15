import configparser
config = configparser.RawConfigParser()
config.read(".//Configuration//config.ini")


class readconfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getusername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        username = config.get('common info', 'invalidUsername')
        return username

    @staticmethod
    def get_invalid_password():
        password = config.get('common info', 'invalidPassword')
        return password
