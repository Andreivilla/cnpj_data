#para realizar os destes python -m unittest service_test.py
import unittest
import api_cnpj_service as api


class Testservice(unittest.TestCase):
    
    def test_get_cnpj_correto(self):
        cnpj = '11187850000167'
        self.assertEqual(api.cnpj_consume(cnpj).json().get('status'), 'OK')

    def test_get_cnpj_incorreto(self):
        cnpj = '11187850000'
        self.assertEqual(api.cnpj_consume(cnpj).json().get('status'), 'ERROR')

