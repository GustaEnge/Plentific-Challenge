from Web_Adapter import Web_Core

class Tests:
    def __init__(self) -> None:
        pass
    def happyPath(self,browser):
        web_adapt = Web_Core()
        web_adapt.Web_Open_Page('Firefox')
        web_adapt.WEB_Get_Credentials('teste01')
        web_adapt.WEB_Login()
        web_adapt.WEB_Choose_Board('Gustavinho')
        web_adapt.WEB_Verify_Cards('To Do','Algo')
        web_adapt.WEB_Verify_Comment()
        web_adapt.WEB_Add_Card('Plentific')
        web_adapt.WEB_Add_Comment('Plentific','Worked!')
        web_adapt.WEB_Set_Start_Due_Date('Casa','11/19/2022','11/19/2022','10:00 PM')     
        web_adapt.WEB_Mark_As_Done('Casa')     

if __name__=='__main__':
    test01 = Tests()
    test01.happyPath('Chrome')
    test01.happyPath('Firefox')