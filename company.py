import api_cnpj_service as api

class company:
    def __init__(self, cnpj):
        self.cnpj = cnpj
        self.data = api.cnpj_consume(self.cnpj)
    
    def data_json(self):
        return self.data.json()