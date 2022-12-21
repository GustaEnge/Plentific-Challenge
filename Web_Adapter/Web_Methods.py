import re
from Web_Actions import * 
from time import sleep
import Locators as locate


class methods:
    def __init__(self) -> None:
        self.element = None
        self.board_id = None
    def login(self,email,password):

            extract_domain = email[:email.index('@')]
            self.driver.get('https://trello.com/login')
            waitPage(self.driver)   
            write_text_by_id(self.driver,'user',email)
            submit(self.driver,'id','login')
            waitPage(self.driver)
            sleep(2)
            write_text_by_xpath(self.driver,"//*[@id='password']",password)
            submit(self.driver,'id','login-submit')
            waitPage(self.driver)
            waitPage(self.driver)
            sleep(2)
            self._validate_parameter('Subdomain',extract_domain,self.driver.current_url)

    def create_new_account(self,email):
        self.driver.get('https://trello.com/signup')
        waitPage(self.driver)   
        write_text_by_id(self.driver,'email',email)

    def generate_credentials(self,name):
        self.driver.get('https://trello.com/power-ups/admin')
        waitPage(self.driver)
        click_button_by_xpath(self.driver,'//*[text() = "New"]')
        write_text_by_name(self.driver,'name',name)
        self.driver.submit()

    def getBackToMainBoardPage(self,url=None):
        self.driver.get(f'https://trello.com/b/{self.board_id}')
        waitPage(self.driver)
    def get_credentials(self,name):
        self.driver.get('https://trello.com/power-ups/admin')
        waitPage(self.driver)
        click_button_by_xpath(self.driver,'//*[text() = "Trello Workspace"]/..//div/a')
        click_button_by_xpath(self.driver,f'//*[text() = "Trello Workspace"]//..//div[text() = "{name}"]')
        click_button_by_xpath(self.driver,'//*[text() = "API key"]')
        
        api_key = get_text_by_xpath(self.driver,'//label[text() = "API key"]/../..//input')
        
        click_button_by_xpath(self.driver,'//*[text() = "Token"]')

        change_tab(self.driver)
        waitPage(self.driver)
        
        click_button_by_xpath(self.driver,'//*[@value = "Allow"]')
    
        sleep(1)

        token = get_text_by_xpath(self.driver,'//pre')

        return api_key,token

    def chooseBoard(self,name):    
        click_button_by_xpath(self.driver,f"//div[@title='{name}']")
        waitPage(self.driver)
        sleep(1)
        self._validate_parameter('Board',name,self.driver.title)
        url = self.driver.current_url
        self.board_id = re.search(r'(\w*)\/[\w_-]*$',url).group(1)
        # implement the method to retrieve board_id
    
    def verifyCards(self,listName,cardName=None,qtd=None):
        self.listName = listName
        self.cardName = cardName
        self.list_element = findElement(self.driver,'xpath',f"{locate.dictionary_locators['list']%self.listName}/../../div[2]/*//span[contains(text(),'#')]/..",True)
    
        if qtd : self._validate_value('Number of Cards',qtd,len(self.list_element))
        if self.cardName:
            verify_each_card = findElement(self.driver,'xpath',f"{locate.dictionary_locators['list']%self.listName}/../../div[2]/*//span[contains(text(),'{self.cardName}')]/..")
            if verify_each_card: return verify_each_card
            else: raise Exception('There is no card with this name.')
        
    def verifyComments(self):
        element = findElement(self.driver,'xpath',f"{locate.dictionary_locators['list']%self.listName}/../../div[2]/*//div[contains(@class,'list-card-details')]//div[@class='badge']",True)
        if not len(element): raise Exception('There is no card with a comment.')

    def addNewCard(self,cardName):
        #Find and hit the Add a card element#
        click_button_by_xpath(self.driver,f"{locate.dictionary_locators['list']%self.listName}/../../div[3]")
        #Insert the name#
        write_text_by_xpath(self.driver,f"//textarea[contains(@class,'list-card')]",cardName)
        #Add the card#
        click_button_by_xpath(self.driver,f"//div[@class='cc-controls-section']/input")

    def addComment(self,cardName,text):
        #Find and go over the card#
        click_button_by_xpath(self.driver,f"{locate.dictionary_locators['list']%self.listName}/../../div[2]/*//span[contains(text(),'{cardName}')]")
        waitPage(self.driver)
        #Find and go over the comment area#
        click_button_by_xpath(self.driver,"//textarea[contains(@class,'comment-box-input js-new-comment-input')]")
        #Write a comment#
        write_text_by_xpath(self.driver,"//textarea[contains(@class,'comment-box-input js-new-comment-input')]",f'{text}')
        #Click on Save Button#
        click_button_by_xpath(self.driver,"//textarea[contains(@class,'comment')]/../div/input")

        #Check if it was added
        if findElement(self.driver,'xpath',f"//div[@class='window-title']/h2[text()='{cardName}']/"):
            elements = findElement(self.driver,"//div[@class='window']//div[contains(@class,'current-comment')]//p",True)
            if not any([text in comment.text for comment in elements]): raise Exception('The comment was not added.')
        sleep(1)
        self.getBackToMainBoardPage()
    def setStartDueDate(self,cardName,startDate,dueDate,timeDueDate):
        click_button_by_xpath(self.driver,f"{locate.dictionary_locators['list']%self.listName}/../../div[2]/*//span[contains(text(),'{cardName}')]")
        waitPage(self.driver)
        #Click on Date Button#
        click_button_by_xpath(self.driver,"//*[@data-testid='card-back-due-date-button']")
        #Select Start Date CheckBox using JS#
        checkBox_mark(self.driver,'xpath',"//label[contains(text(),'Start date')]/../label[2]/input")
        #Insert in Start Date#
        write_text_by_xpath(self.driver,"//label[contains(text(),'Start date')]/../div/input",startDate)
        #Select Start Date CheckBox#
        checkBox_mark(self.driver,'xpath',"//label[contains(text(),'Start date')]/../label[2]/input")
        #Insert in Due Date the Date part#
        write_text_by_xpath(self.driver,"//label[contains(text(),'Due date')]/../div/input[@data-testid='due-date-field']",dueDate)
        #Insert in Due Date the Time part#
        write_text_by_xpath(self.driver,"//label[contains(text(),'Due date')]/../div/input[@placeholder='Add time']",timeDueDate)
        #Click on Save Button#
        click_button_by_xpath(self.driver,"//button[@type='submit']")
        self.getBackToMainBoardPage()

    def markAsDone(self,cardName):
        checkBox_mark(self.driver,'xpath',f"{locate.dictionary_locators['list']%self.listName}/../../div[2]/*//span[contains(text(),'{cardName}')]/../div[2]")
        sleep(0.5)
    
    def _validate_parameter(self, name, system,web):
        if system not in web:
            raise AssertionError('%s is different. System is %s. WEB is %s' % (name, system,web))    

    def _validate_value(self,name,system,web):
        if system != web:
            raise AssertionError('%s is different. System is %s. WEB is %s' % (name, system,web))
'''
    a = $x("/html/.//h2[contains(text(), 'To Do')]/../../div[2]/*")
    a[0].childElementCount


    //h2[contains(text(), 'To Do')]/../../div[2]/*//div[@class='badges']
    //h2[contains(text(), 'To Do')]/../../div[2]/a/div[3]/span[contains(text(),'Tratar')]
    //span[contains(text(),'#')]/..
    //div[contains(@class,'list-card-details')]//div[@class='badge']
    //h2[contains(text(), 'To Do')]/../../div[2]/*//span[contains(text(),'Tratar desse assunto')]/..
    //h2[contains(text(), 'To Do')]/../../div[2]/*//div[contains(@class,'list-card-details')]//div[@class='badge']
    //div[@class='window']//div[contains(@class,'current-comment')]//p
'''