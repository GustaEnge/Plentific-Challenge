import json
import re

class boards():

    def __init__(self) -> None:
        pass

    def get_board(self,board_id):
        '''
        Returns an specific board from Trello account
            Parameters:
                    board_id (string) : board id
            Returns:
                   A single board if it worked (200 code) otherwise will return the error code
        '''
        headers = { 'accept': "application/json" }

        result = self.session.get(self.url+"boards/"+board_id,headers=headers,params= self.params)
        if result.status_code == 200:
            print(result.text)
            return json.loads(result.text)
        else: 
            error = f"error {result.status_code} : {result.content.decode('UTF-8')}"
            raise Exception(error)
    

    def create_board(self,**kwargs):
        '''
        Creates a board from Trello account
            Parameters:
                    name (string) : the name you wanna give for your new board
            Returns:
                   A single board if it worked (200 code) otherwise will return the error code
        '''
        headers = { 'accept': "application/json" }
        params = self.params
        params.update(kwargs)

        result = self.session.post(self.url+"boards",headers=headers,params=params)
        if result.status_code == 200:
            res = json.loads(result.text)
            url = res['url']
            id = res['id']
            print(url)
            id_web = re.search(r'(\w*)\/[\w_-]*$',url).group(1)
            return id_web,id
        else: 
            error = f"error {result.status_code} : {result.content.decode('UTF-8')}"
            raise Exception(error)

    def update_board(self,id,**kwargs):
        '''
        Updates a board from Trello account
            Parameters:
                    board_id (string) : board id
            Returns:
                   A single board if it worked (200 code) otherwise will return the error code
        '''
        headers = { 'accept': "application/json" }

        params = self.params
        params.update(kwargs)

        result = self.session.put(self.url+f"boards/{id}",headers=headers,params=params)
        if result.status_code == 200:
            return result.text
        else: 
            error = f"error {result.status_code} : {result.content.decode('UTF-8')}"
            raise Exception(error)
        
        
    def delete_board(self,id):
        '''
        Deletes a board from Trello account
            Parameters:
                    board_id (string) : board id
            Returns:
                   200 code otherwise will return the error code
        '''
        headers = { 'accept': "application/json" }

        result = self.session.delete(self.url+f"boards/{id}",headers=headers,params=self.params)
        if result.status_code == 200:
            return result.text
        else: 
            error = f"error {result.status_code} : {result.content.decode('UTF-8')}"
            raise Exception(error)