import http.client
import requests
import ssl
import os,sys
import subprocess
from Lib_boards import boards
from Lib_actions import actions
from Lib_cards import cards
from Lib_lists import lists

cwd = os.getcwd()+'/Settings'

sys.path.append(cwd)
from config import Config
#home = expanduser('~')
dir_path = os.path.dirname(os.path.realpath(__file__))

class API_Core(boards,cards,lists,actions):
    ROBOT_LIBRARY_SCOPE = 'SUITE'
    def __init__(self,account='default',api_key=None,token=None) -> None:
        #self.session = requests.Session()
        self.url = "https://api.trello.com/1/"

        if account == 'default':
            config = Config()
            credentials = config.getAccounts(account)
            self.api_key = credentials['default']['api_key']
            self.token = credentials['default']['token']
        if account == 'new': pass    
        self.params = {'key':self.api_key,'token':self.token}
        #self.list_id = None
        
        super(API_Core, self).__init__()


    def save_screenshot(self):
        { 
            "api_key":"",
            "token":"",
            "id_board_web":"",
            "id_board":"",
            "id_list":"",
            "id_card":"",
            "date_creation":"",
            "date_modification":""

        }      
    def API_Create_Board(self,**kwargs):
        return self.create_board(**kwargs)

    def API_Get_Board(self,idBoard):
        return self.get_board(idBoard)

    def API_Update_Board(self,id,**kwargs):
        return self.update_board(id,**kwargs)

    def API_Delete_Board(self,idBoard):
        return self.delete_board(idBoard)    

    def API_Create_Card(self,**kwargs):
        return self.create_card(**kwargs)
    
    def API_Get_Card(self,idCard):
        return self.get_card(idCard) 
      
    def API_Get_All_Card(self,idList,name):
        return self.get_all_cards(idList,name)               

    def API_Update_Card(self,idCard,**kwargs):
        return self.update_card(idCard,**kwargs)

    def API_Delete_Card(self,idCard):
        return self.delete_card(idCard)

    def API_Create_Comment(self,id_card,name):
        return self.create_comment(id_card,name)

    def API_List_Create(self,**kwargs):
        print(kwargs)
        return self.listCreate(**kwargs)
    
    def API_Get_List(self,idCard):
        return self.get_list(idCard)

    def API_Get_Lists(self,idBoard,name):
        return self.getLists(idBoard,name)            

    def API_Update_List(self,id_list,**kwargs):
        return self.update_list(id_list,**kwargs)

    def API_Archive_List(self,idCard,value):
        return self.archive_list(idCard,value)    
 
if __name__ == "__main__":
    api_test = API_Core('default')
    #api_test.API_Get_Board('IjCWTxQr')
    #id,code = api_test.API_Create_Board(name='Plentific Board')
    #api_test.API_Update_Board('eXfA4ILY',name='Main Board')
    #api_test.API_Delete_Board('eXfA4ILY')
    # id_web -> 'eXfA4ILY' | id_api -> 63a0e7c2b76ac90102557d40
    #id_list = api_test.API_Get_Lists('eXfA4ILY','TopListView')
    #api_test.API_List_Create(name='TopList',idBoard='63a2319f416b4901088ad9e2')
    #api_test.API_Update_List(id_list,name='TopListView')
    #api_test.API_Archive_List(id_list,'false')
    #id,result= api_test.API_Create_Card(name='Java Validation',idList=id_list)
    #api_test.API_Get_Card('63a11812facac20b2560cd88')
    #api_test.API_Update_Card('63a11812facac20b2560cd88',name='Python Validation')
    #id_card = api_test.API_Get_All_Card('63a11095d328fa0067d902f9','Python Validation')
    #api_test.API_Delete_Card(id_card)
    #api_test.API_Create_Comment(id_card,"Worked! 2022")