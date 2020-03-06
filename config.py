import json
from os import path, urandom
from colorama import init, Fore
from base64 import b64encode
init() #Colorama thing
DefaultConfig = { #THESE ARE DEFAULT OPRIONS FOR THE CONFIG.
    "Port" : 1337,
    #SQL Info
    "SQLHost" : "localhost",
    "SQLUser" : "",
    "SQLDatabase" : "ripple",
    "SQLPassword" : "",
    #Redis Info
    "RedisHost" : "localhost",
    "RedisPort" : 6379,
    "RedisDb" : 0,
    #Server Settings
    "ServerName" : "osu!Shibui",
    "ServerURL" : "https://shibui.pw/",
    "LetsAPI" : "https://127.0.0.1:5002/letsapi/",
    "AvatarServer" : "https://a.shibui.pw/",
    "BanchoURL" : "https://c.shibui.pw/",
    "BeatmapMirror" : "http://storage.kurikku.pw/",
    "IpLookup" : "http://ip.zxq.co/",
    "HasRelax" : True,
    "AvatarDir" : "/root/ripple/avatars/avatars/",
    "Webhook" : "", #Discord webhook for posting newly ranked maps
    #Recaptcha v2 for the login page
    "UseRecaptcha" : False,
    "RecaptchaSecret" : "",
    "RecaptchaSiteKey" : "",
    #RealistikPanel Settings
    "PageSize" : 50, #number of elements per page
    "SecretKey" : b64encode(urandom(64)).decode('utf-8') #generates random encryption key
}

class JsonFile:
    @classmethod
    def SaveDict(self, Dict, File="config.json"):
        """Saves a dict as a file"""
        with open(File, 'w') as json_file:
            json.dump(Dict, json_file, indent=4)

    @classmethod
    def GetDict(self, File="config.json"):
        """Returns a dict from file name"""
        if not path.exists(File):
            return {}
        else:
            with open(File) as f:
                data = json.load(f)
            return data

UserConfig = JsonFile.GetDict("config.json")
#Config Checks
if UserConfig == {}:
    print(Fore.YELLOW+" No config found! Generating!"+Fore.RESET)
    JsonFile.SaveDict(DefaultConfig, "config.json")
    print(Fore.WHITE+" Config created! It is named config.json. Edit it accordingly and start RealistikPanel again!")
    exit()
else:
    #config check and updater
    AllGood = True
    NeedSet = []
    for key in list(DefaultConfig.keys()):
        if key not in list(UserConfig.keys()):
            AllGood = False
            NeedSet.append(key)

    if AllGood:
        print(Fore.GREEN+" Configuration loaded successfully! Loading..." + Fore.RESET)
    else:
        #fixes config
        print(Fore.BLUE+" Updating config..." + Fore.RESET)
        for Key in NeedSet:
            UserConfig[Key] = DefaultConfig[Key]
            print(Fore.BLUE+f" Option {Key} added to config. Set default to '{DefaultConfig[Key]}'." + Fore.RESET)
        print(Fore.GREEN+" Config updated! Please edit the new values to your liking." + Fore.RESET)
        JsonFile.SaveDict(UserConfig, "config.json")
        exit()
        
