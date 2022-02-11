from configparser import ConfigParser
import ConfigurationData




def readConfig(section,key):
    config = ConfigParser()
    config.read("C:\\pythonProject\\UI\\ConfigurationData\\config.ini")
    return config.get(section,key)


# print(readConfig("locator","newcar_XPATH"))
# print(readConfig("URL","url"))