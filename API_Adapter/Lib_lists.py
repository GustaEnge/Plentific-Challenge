import json

class lists():

    def __init__(self) -> None:
        pass

    def getLists(self,board_id,nameList=None):
        '''
        Returns all lists from Trello account
            Parameters:
                    board_id (string) : board id
                    find (bool) : if it's True, it will search for a specific list
                    nameList (string) : list's name that you want to search from
            Returns:
                   All lists if it worked (200 code) otherwise will return the error code
        '''
        headers = { 'accept': "application/json" }

        result = self.session.get(self.url+f"/boards/{board_id}/lists",headers=headers,params=self.params)
        if result.status_code == 200:
            if nameList:
                lists = list((each_list["name"],each_list["id"]) for each_list in (json.loads(result.text)))
                search = dict(lists).get(nameList,None)
                if search: return search
                else:  raise Exception("There is no list with this name")
            return result.text
        else: 
            error = f"error {result.status_code} : {result.content.decode('UTF-8')}"
            raise Exception(error)
    def get_list(self,list_id):
        '''
        Returns an specific list from Trello account
            Parameters:
                    list_id (string) : list id
            Returns:
                   A single list if it worked (200 code) otherwise will return the error code
        '''
        headers = { 'accept': "application/json" }

        result = self.session.get(self.url+"lists/"+list_id,headers=headers,params= self.params)
        if result.status_code == 200:
            return result.text
        else: 
            error = f"error {result.status_code} : {result.content.decode('UTF-8')}"
            raise Exception(error)
    

    def listCreate(self,**kwargs):
        '''
        Creates a list from Trello account
            Parameters:
                    name (string) : the name you want to give for your new list
                    id : the board id where you want to create the list from 
            Returns:
                    A single list if it worked (200 code) otherwise will return the error code
            Example (params):
                    name='List1',id=ahda756
        '''
        headers = { 'accept': "application/json" }
        params = self.params
        params.update(kwargs)

        result = self.session.post(self.url+"lists",headers=headers,params=params)
        if result.status_code == 200:
            id = (json.loads(result.text))['id']
            return id,result.status_code
        else: 
            error = f"error {result.status_code} : {result.content.decode('UTF-8')}"
            raise Exception(error)

    def update_list(self,id,**kwargs):
        '''
        Updates a list from Trello account
            Parameters:
                    list_id (string) : list id
            Returns:
                   A single list if it worked (200 code) otherwise will return the error code
        '''
        headers = { 'accept': "application/json" }
        params = self.params
        params.update(kwargs)

        result = self.session.put(self.url+f"lists/{id}",headers=headers,params=params)
        if result.status_code == 200:
            return result.text
        else: 
            error = f"error {result.status_code} : {result.content.decode('UTF-8')}"
            raise Exception(error)
        
        
    def archive_list(self,idList,value):
        '''
        Deletes a list from Trello account
            Parameters:
                    list_id (string) : list id
                    value (bool) : True if you want to archive otherwise unarchive, depending on the state 
            Returns:
                   200 code otherwise will return the error code
        '''
        params = self.params
        params.update({"value":value})
        headers = { 'accept': "application/json" }

        result = self.session.put(self.url+f"lists/{idList}/closed",headers=headers,params = self.params)
        if result.status_code == 200:
            return result.text
        else: 
            error = f"error {result.status_code} : {result.content.decode('UTF-8')}"
            raise Exception(error)