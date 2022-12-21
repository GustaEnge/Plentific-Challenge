import os,sys
import pathlib
from Web_Methods import methods
import os
from selenium import webdriver
from Web_Actions import *
from selenium import webdriver
import os
cwd = os.getcwd()+r'\Settings'
sys.path.append(cwd)

from config import Config

class Web_Core(methods):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self,browser,account='default',before=False) -> None:
        self.url = "https://trello.com/"
        self.driver = None
        self.browser = browser
        if before : self._open_page(browser)

        if account == 'default':
            config = Config()
            credentials = config.getAccounts(account)
            self.api_key = credentials['default']['api_key']
            self.token = credentials['default']['token']

            self.email = credentials['default']['email']
            self.password = credentials['default']['password']
        if account == 'new': pass   

        super(Web_Core, self).__init__()

    def _open_page(self,browser,headless=False):
        '''
            Set up the web object to open the proper URL
                Parameters:
                        headless (boolean) : whether it will be opened with UI or not 
                Returns:
                    the driver instantiated
        '''             
        if browser == 'Firefox':
            self.driver = webdriver.Firefox()
            self.driver.set_window_position(2000,0)  
        if browser == 'Chrome':
           
            options = webdriver.ChromeOptions()
            if not headless:
                options.add_argument("--window-position=2000,0")
                self.driver = webdriver.Chrome(options=options)
            else:
                options.headless = True
                driver = webdriver.Chrome(executable_path=cwd+r'\\Drivers\\chromedriver.exe',options=options)
        
        self.driver.get(self.url)
        self.driver.maximize_window()  
    
    def _close_page(self,):
        self.driver.quit()
    def __exit__(self):
        self._close_page(self)

    def WEB_Get_Credentials(self,name,):
        #if driver:self.driver = driver
        return self.get_credentials(name)

    def Web_Open_Page(self):
        self._open_page(self.browser)
        
    def Web_Close_Page(self,):
        self._close_page(self) 

    def WEB_Login(self,email=None,password=None,):
        email,password = email,password
        if self.email and self.password: 
            email,password = self.email,self.password    
        self.login(email,password)

    def WEB_Choose_Board(self,name,):
        self.chooseBoard(name)
      

    def WEB_Verify_Cards(self,listName,cardName,):
        self.verifyCards(listName,cardName)

    def WEB_Verify_Comment(self,):
        self.verifyComments()

    def WEB_Add_Comment(self,cardName,text,):
        self.addComment(cardName,text) 

    def WEB_Set_Start_Due_Date(self,cardName,startDate,dueDate,timeDueDate,):
        return self.setStartDueDate(cardName,startDate,dueDate,timeDueDate)
 
    def WEB_Mark_As_Done(self,cardName,):
        self.markAsDone(cardName)

    def WEB_Add_Card(self,cardName,):
        self.addNewCard(cardName)

if __name__ == "__main__":
    obj = Web_Core('Chrome','default')

    obj.Web_Open_Page()
    #obj.WEB_Get_Credentials('teste01')
    obj.WEB_Login()
    obj.WEB_Choose_Board('Gustavinho')
    obj.WEB_Verify_Cards('To Do','Algo')
    obj.WEB_Verify_Comment()
    obj.WEB_Add_Card('Plentific')
    obj.WEB_Add_Comment('Plentific','Worked!')
    obj.WEB_Set_Start_Due_Date('Casa','11/19/2022','11/19/2022','10:00 PM')     
    obj.WEB_Mark_As_Done('Casa')     