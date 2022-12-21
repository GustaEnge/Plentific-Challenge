import json

class actions():

    def __init__(self) -> None:
        pass

    def get_card(self,board_id):
        '''
        Returns an specific card from one board
            Parameters:
                    card_id (string) : card id
            Returns:
                   A single card if it worked (200 code) otherwise will return the error code
        '''
        headers = { 'accept': "application/json" }

        result = self.session.get(self.url+"boards/"+board_id,headers=headers,params= self.params)
        if result.status_code == 200:
            return result.text
        else: 
            error = f"error {result.status_code} : {result.content.decode('UTF-8')}"
            raise Exception(error)
    

    def create_action(self,name,*kwargs):
        '''
        Creates a board from Trello account
            Parameters:
                    name (string) : the name you wanna give for your new board
            Returns:
                   A single board if it worked (200 code) otherwise will return the error code
        '''
        headers = { 'accept': "application/json" }
        params = self.params

        payload = json.dumps(kwargs)

        result = self.session.post(self.url+"boards",headers=headers,params=params.update({'name':name}),payload=payload)
        if result.status_code == 200:
            return result.text
        else: 
            error = f"error {result.status_code} : {result.content.decode('UTF-8')}"
            raise Exception(error)

    def create_comment(self,id_card,text):
        '''
        Creates a comment inside a card
            Parameters:
                id_card (string) : the card id you want to add a comment
                text (string) : the text you want to write
            Returns:
               The card you added the comment if it worked (200 code) otherwise will return the error code
        '''
        headers = { 'accept': "application/json" }
        params = self.params
        params.update({'text':text})

        result = self.session.post(self.url+f"cards/{id_card}/actions/comments",headers=headers,params=params)
        if result.status_code == 200:
            return result.text
        else: 
            error = f"error {result.status_code} : {result.content.decode('UTF-8')}"
            raise Exception(error)            

    def update_board(self,id,*kwargs):
        '''
        Updates a board from Trello account
            Parameters:
                    board_id (string) : board id
            Returns:
                   A single board if it worked (200 code) otherwise will return the error code
        '''
        headers = { 'accept': "application/json" }

        payload = json.dumps(kwargs)

        result = self.session.put(self.url+f"boards/{id}",headers=headers,params=self.params,payload=payload)
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

        result = self.session.post(self.url+f"boards/{id}",headers=headers)
        if result.status_code == 200:
            return result.text
        else: 
            error = f"error {result.status_code} : {result.content.decode('UTF-8')}"
            raise Exception(error)