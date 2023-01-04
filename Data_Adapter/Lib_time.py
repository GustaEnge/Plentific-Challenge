import time
import string,re
import datetime as date

class Fields:
    def _init_(self,type=None) -> None:
        self.type = type
        self.value = ""
    def timeConverter(self,data=None):
        data = self.value if data == None else data
        if data.isnumeric() or re.search(r'\d+\.\d+',data) != None:
            self.value = (date.datetime.fromtimestamp(float(data))).strftime("%d/%m/%Y %H:%M:%S")
            return self.value
        elif "/" in data:
            new_date = time.mktime(date.datetime.strptime(data, "%d/%m/%Y %H:%M:%S").timetuple())
            self.value = new_date
            return self.value

    def getTimeNow(self,s=0,m=0,h=0,d=0,pattern="%d/%m/%Y %H:%M:%S"):
        now = date.datetime.now()
        new_value = now
        if any(map(lambda i:i != 0,[s,m,h,d])):
            new_value = now + date.timedelta(seconds=s,minutes=m,hours=h,days=d)
        self.value = new_value.strftime(pattern)
        return self
        
    def getAccoundId_DocType_Dynamo(self,id,doc):
        return f'{id}::{doc}'

if _name_ == "_main_":
    obj = Fields("time")    
    #print(obj.timeConverter('2635225961'))
    #print(obj.timeConverter('26/10/2021 02:26:00'))
    print(obj.getTimeNow(0,20).timeConverter())