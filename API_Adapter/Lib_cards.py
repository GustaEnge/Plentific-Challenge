import json

class cards():

    def __init__(self) -> None:
        pass

    def get_all_cards(self,list_id,nameCard=None):
        '''
        Returns an specific card from one board
            Parameters:
                    card_id (string) : card id
                    find (bool) : if it's True, it will search for a specific card
                    nameCard (string) : card's name that you want to search from
            Returns:
                   A single card if it worked (200 code) otherwise will return the error code
        '''
        headers = { 'accept': "application/json" }

        result = self.session.get(self.url+f"lists/{list_id}/cards/",headers=headers,params= self.params)
        if result.status_code == 200:
            if nameCard:
                cards = list((each_card["name"],each_card["id"]) for each_card in (json.loads(result.text)))
                search = dict(cards).get(nameCard,None)
                if search: return search
                else:  raise Exception("There is no card with this name")
            return result.text
        else: 
            error = f"error {result.status_code} : {result.content.decode('UTF-8')}"
            raise Exception(error)

    def get_card(self,card_id):
        '''
        Returns an specific card from one board
            Parameters:
                    card_id (string) : card id
            Returns:
                   A single card if it worked (200 code) otherwise will return the error code
        '''
        headers = { 'accept': "application/json" }

        result = self.session.get(self.url+"cards/"+card_id,headers=headers,params= self.params)
        if result.status_code == 200:
            return result.text
        else: 
            error = f"error {result.status_code} : {result.content.decode('UTF-8')}"
            raise Exception(error)
    

    def create_card(self,**kwargs):
        '''
        Creates a card from one board
            Parameters:
                    name (string) : the name you wanna give for your new board
            Returns:
                   A single card if it worked (200 code) otherwise will return the error code
        '''
        headers = { 'accept': "application/json" }
        params = self.params
        params.update(kwargs)

        result = self.session.post(self.url+"cards",headers=headers,params=params)
        if result.status_code == 200:
            res = json.loads(result.text)
            id = res['id']
            return id,result.status_code
        else: 
            error = f"error {result.status_code} : {result.content.decode('UTF-8')}"
            raise Exception(error)

    def update_card(self,card_id,**kwargs):
        '''
        Updates a card from Trello account
            Parameters:
                    board_id (string) : card id
            Returns:
                   A card if it worked (200 code) otherwise will return the error code
        '''
        headers = { 'accept': "application/json" }

        params = self.params
        params.update(kwargs)

        result = self.session.put(self.url+f"cards/{card_id}",headers=headers,params=self.params)
        if result.status_code == 200:
            return result.text
        else: 
            error = f"error {result.status_code} : {result.content.decode('UTF-8')}"
            raise Exception(error)
        
        
    def delete_card(self,card_id):
        '''
        Deletes a card from one board
            Parameters:
                    board_id (string) : board id
            Returns:
                   200 code otherwise will return the error code
        '''
        headers = { 'accept': "application/json" }

        result = self.session.delete(self.url+f"cards/{card_id}",headers=headers,params=self.params)
        if result.status_code == 200:
            return result.text
        else: 
            error = f"error {result.status_code} : {result.content.decode('UTF-8')}"
            raise Exception(error)