import os,sys
from Web_Methods import methods
import os
from selenium import webdriver
from Web_Actions import * 

dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+r'\Settings\\'
sys.path.append(dir_path)

from config import Config

class Web_Core(methods):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self,browser,account='default') -> None:
        self.url = "https://trello.com/"
        self.driver = None
        self.browser = browser
        self._open_page(browser)

        if account == 'default':
            config = Config()
            credentials = config.getAccounts(account)
            self.api_key = credentials['default']['api_key']
            self.token = credentials['default']['token']

            self.email = credentials['default']['email']
            self.password = credentials['default']['password']
        if account == 'new': pass   

        super(Web_Core, self).__init__()

    def _open_page(self,browser='Chrome',headless=False):
        '''
            Set up the web object to open the proper URL
                Parameters:
                        headless (boolean) : whether it will be opened with UI or not 
                Returns:
                    the driver instantiated
        '''             
        if browser == 'Firefox':
            self.driver = webdriver.Firefox()  
        # if browser == 'Chrome':

        #     options = webdriver.ChromeOptions()
        #     s = Service(ChromeDriverManager().install())
        #     if not headless:
        #         options.add_argument("--window-position=2000,0")
        #         driver = webdriver.Chrome(service=s,options=options)
        #     else:
        #         options.headless = True
        #         driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.set_window_position(2000,0)
        self.driver.get(self.url)
        self.driver.maximize_window()  
    
    def _close_page(self,driver=None):
        self.driver.quit() if self.driver else driver.quit()
    def __exit__(self):
        self._close_page(self)

    def WEB_Get_Credentials(self,name,driver=None):
        #if driver:self.driver = driver
        return self.get_credentials(name)

    def Web_Open_Page(self,driver=None):
        self._open_page(self,self.browser)
        
    def Web_Close_Page(self,driver=None):
        self._close_page(self) 

    def WEB_Login(self,email=None,password=None,driver=None):
        email,password = email,password
        if self.email and self.password: 
            email,password = self.email,self.password    
        self.login(email,password)

    def WEB_Choose_Board(self,name,driver=None):
        self.chooseBoard(name)
      

    def WEB_Verify_Cards(self,listName,cardName,driver=None):
        self.verifyCards(listName,cardName)

    def WEB_Verify_Comment(self,driver=None):
        self.verifyComments()

    def WEB_Add_Comment(self,cardName,text,driver=None):
        self.addComment(cardName,text) 

    def WEB_Set_Start_Due_Date(self,cardName,startDate,dueDate,timeDueDate,driver=None):
        return self.setStartDueDate(cardName,startDate,dueDate,timeDueDate)
 
    def WEB_Mark_As_Done(self,cardName,driver=None):
        self.markAsDone(cardName)

    def WEB_Add_Card(self,cardName,driver=None):
        self.addNewCard(cardName)

if __name__ == "__main__":
    obj = Web_Core('default')

    obj.Web_Open_Page('Firefox')
    obj.WEB_Get_Credentials('teste01')
    obj.WEB_Login()
    obj.WEB_Choose_Board('Gustavinho')
    obj.WEB_Verify_Cards('To Do','Algo')
    obj.WEB_Verify_Comment()
    obj.WEB_Add_Card('Plentific')
    obj.WEB_Add_Comment('Plentific','Worked!')
    obj.WEB_Set_Start_Due_Date('Casa','11/19/2022','11/19/2022','10:00 PM')     
    obj.WEB_Mark_As_Done('Casa')     