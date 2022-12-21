from base64 import decode
import time
import requests
#grequests
import json
import http.client
import random,re
from Data_Adapter import Lib_db as dbmock
from bs4 import BeautifulSoup
from requests import status_codes
from faker import Faker


dictionary_model = ["id","first_name","last_name","organization_name","phone","email","password","fiscal_id","address","postal_code","city","tax_country","language","force","terms","marketing"]
data_batch = []
class User:
    url_mock_company =""
    url_pwsd =""
    dict_response = ""
    dict_user = {}
    
    def __init__(self) -> None:
        self.url_mock_company,self.url_pwsd = "https://fakerapi.it/api/v1/companies?_quantity=1","https://api.namefake.com/random/random"
        
    def getApi(self,url):        

        payload={}
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        self.dict_response = json.loads(response.text)
    def getApiHtml(self,url):
        time.sleep(1)        
        response = requests.get(url)
        return response.text if response.status_code == 200 else None

    def generatePTAccount(self,return_result='1',mode='list', mail=None, pswd=None):
        dict_var = {}
        attrs = ['firstName','lastName','company','phone','email','password','vat','country','language','tax_country','force','address','zipcode','city','website','shareCapital','terms']
        soup = BeautifulSoup(self.getApiHtml('https://nif.marcosantos.me/'),'html.parser')
        tag = soup.body.find('h2',attrs={'id':"nif"})
        pattern = r"\d{4}-\d{3}"
        self.getApi(self.url_mock_company)
        self.dict_user = self.dict_response['data'][0]
        id_account = str(random.randint(0,100000))
        company_name = self.dict_user['name']
        first = self.dict_user['contact']['firstname']
        last = name = self.dict_user['contact']['lastname']
        email = self.dict_user['email']
        website = self.dict_user["website"]
        share_capital = float(random.randint(10,999999))
        fake = Faker('pt_PT')
        vat_number = tag.contents[0]
        #'222415266'
        re.search("\d+",fake.vat_id()).group(0)
        city = fake.city_name().replace('\n','')
        address = fake.address()
        valid_address = re.sub(pattern,"",fake.address()).replace('\n','')
        zip = re.search(pattern,address).group(0)
        phone_number = fake.phone_number().replace('(351)','').replace(' ','')
        password = self.getPassword() 

        arguments = [first,last,company_name,phone_number,email,password,vat_number,"Portugal",'pt','1','false',valid_address,zip,city] if mode in ['list','dict'] else [id_account,first,last,company_name,phone_number,email,password,vat_number,valid_address,zip,city,'1','pt','false','1','0'] if mode == 'json' else None
        arguments = [a.replace(',','') for a in arguments]
        arguments[4] = mail if mail != None else arguments[4] 
        arguments[5] = pswd if pswd != None else arguments[5]
        arguments[11] = arguments[11].replace('\n','')
        if mode == 'dict':
            arguments += [website,share_capital,"1"] 
            dict_attrs = {attrs[i]:arguments[i] for i in range(len(arguments))}

        if return_result == '1':
            return arguments if mode != 'dict' else dict_attrs
        if return_result == 'many':
            #arguments = [id_account,first,last,company_name,phone_number,email,password,vat_number,"Portugal",'pt','1','false',valid_address.decode(),zip,city.decode()] if mode == 'list' else [id_account,first,last,company_name,phone_number,email,password,vat_number,valid_address.decode(),zip,city.decode(),'1','pt','false','1','0'] if mode == 'json' else None
            dict_var = {dictionary_model[i]:arguments[i] for i in range(len(dictionary_model))}
            data_batch.append(dict_var)
            return json.dumps(dict_var)

    def retrieveDataBatch(self,mode='json'):
        if mode == 'json':
           f = open("/Users/gustavocunha/Github/InvoiceXpress_Test_Automation_FW/accounts.txt", "a")
           f.write(json.dumps(data_batch))
           f.close()
   
    def generateAccount(self,return_result='1'):
    
        self.getApi(self.url_mock_company)
        self.dict_user = self.dict_response['data'][0]
        position = random.randint(0,len(self.dict_user['addresses'])-1)    
        
        company_name = self.dict_user['name']
        first = self.dict_user['contact']['firstname']
        last  = self.dict_user['contact']['lastname']
        email = self.dict_user['email']
        country = self.dict_user['addresses'][position]['country']
        phone = self.dict_user['phone']
        name  = self.dict_user['contact']['firstname']+" "+self.dict_user['contact']['lastname']
        vat = self.dict_user['vat']
        address = ", ".join([v for k,v in self.dict_user['addresses'][position].items() if k in ["street","streetName","buildingNumber"]])
        city = self.dict_user['addresses'][position]["city"]
        zipCode = self.dict_user['addresses'][position]["zipcode"]
        website = self.dict_user["website"]
        share_capital = float(random.randint(10,999999))
        password = self.getPassword()


        if return_result == '1':
            return [company_name,first,last,email,password,country,vat,address,zipCode,city,website,share_capital,phone]
        if return_result == 'many':
            data_batch.append(tuple([company_name,first,last,email,password,country,vat,address,zipCode,city,website,share_capital,phone]))



    def getPassword(self):
        self.getApi(self.url_pwsd)
        while ("'" in self.dict_response["password"]):
            self.getApi(self.url_pwsd)
        return self.dict_response["password"]

    def DBHandler(self,type):
        DB = dbmock.DataBase(type)
        DB.insertManyDB(data_batch)

    def DBInsert(self,list_var,type='sqlite'):    
        DB = dbmock.DataBase(type)
        DB.insertDB(list_var)

    def DBUpdate(self,list_var,type='sqlite'):
        DB = dbmock.DataBase(type)
        DB.updateDB(list_var)

    def DBSelect (self,method,value=None,type='sqlite'):
        DB = dbmock.DataBase(type)
        
        if method == 'getId' : return DB.getLastID()
        else: return DB.readAccount(value)
        
    def generateObjects(self,number):
        objs = [User() for i in range(number)]
        for obj in objs:
            obj.generateAccount()
            obj.generatePTAccount()

def main():
    objs = User()
    objs.generateObjects(3)
    objs.DBHandler('sqlite')    
    

if __name__=="__main__":
    main()