import json,os,sys
class Config:
    def __init__(self) -> None:
        pass
    def getAccounts(self,name='default'):
        file = open(os.getcwd()+r'\Settings\accounts.json','r')
        content = json.load(file)
        return content 