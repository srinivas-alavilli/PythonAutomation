import configparser

config = configparser.ConfigParser()
config.read(r".\\Configuration\\config.ini")


# Reading common values from ini file
class ReadConfig():
    @staticmethod
    def get_Application_URL():
        url = config.get('common info','baseUrl')
        return url

    @staticmethod
    def get_UserName():
        username = config.get('common info','username')
        return username

    @staticmethod
    def get_Password():
        password = config.get('common info','password')
        return password
