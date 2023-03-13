import requests
import sys

def cnpj_consume(cnpj):
    url = 'https://receitaws.com.br/v1/cnpj/' #url api
    try:
        req = requests.get(url + cnpj)
        req.raise_for_status() 
    except requests.exceptions.HTTPError as http_error:
        print(f'Erro HTTP: {http_error}')
        raise 
    except requests.exceptions.Timeout as timeout_error:
        print(f'Erro de timeout: {timeout_error}')
        raise
    except requests.exceptions.ConnectionError as connection_error:
        print(f'Erro de conexão: {connection_error}')
        raise
    except requests.exceptions.RequestException as error:
        print(f'Erro: {error}')
        raise
    
    return req