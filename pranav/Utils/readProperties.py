import configparser

config = configparser.RawConfigParser()
config.read(".\\Configs/Config.ini")

class ReadConfig():

    @staticmethod
    def getURL():
        URL = config.get('common_info','baseURL')
        return URL

    @staticmethod
    def getuserName():
        username = config.get('common_info','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common_info','password')
        password.encode(encoding='UTF-16',errors='Strict').decode(encoding='UTF16',errors='Strict')
        return password

    @staticmethod
    def getDriver():
        driver = config.get('common_info','driver')
        return driver

    @staticmethod
    def getadminTitle():
        title = config.get('common_info','admin_title')
        return title

    @staticmethod
    def getloginTitle():
        title1 = config.get('common_info', 'login_title')
        return title1

