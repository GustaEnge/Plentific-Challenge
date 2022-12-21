import json,os,sys
class Config:
    def __init__(self) -> None:
        pass
    def getAccounts(self,name='default'):
        file = open(os.path.dirname(os.path.dirname(os.getcwd()))+r'\Settings\accounts.json','r')
        content = json.load(file)
        return content 