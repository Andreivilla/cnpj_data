# cnpj_data

# Sobre o projeto

cnpj_data é uma aplicação simples para consumir a API ReceitaWS API e retornar todos os dados de uma empresa através de seu CNPJ.

A aplicação consiste em um programa principal get_company_data.py que ao ser chamado e receber um cnpj printa todos os dados de uma empresa bem como gera um pdf simplificado para facilitar a leitura dos dados.

# Tecnologias utilizadas
## API
- ReceitaWS API
## Bibliotecas utilizadas 
- requests disponível em:  https://pypi.org/project/requests/
- reportlab disponível em: https://pypi.org/project/reportlab/
- unittest disponível em: https://docs.python.org/pt-br/3/library/unittest.html

## Função e arquivos

- api_cnpj_service.py 
  * Possui apenas uma função def cnpj_consume(cnpj) que recebe cnpj trata erros da API e retorna sua requisição

- company.py 
  * Utiliza a função de api_cnpj_service.py para retornar os dados em formato json através do método data_json(self)

- pdf_maker.py  
  * Possui uma classe responsável por produzir um pdf com os dados da empresa. O construtor da classe recebe os dados em formato json.
  
- def mm_to_p(self, mm) 
  *  Converte milímetro em pontos da biblioteca reportlab.
  
- def make_string(self) 
  *  Converte os dados json em uma. string para ser impressa no pdf
  
- def make_pdf(self) 
  *   Efetivamente cria o pdf e é chamada no arquivo get_company_data.py.

- get_company_data.py 
  * O arquivo principal do programa cria uma company faz um print de seus dados e utiliza pdf_maker para gerar um pdf.

- service_tesst.py  
  * Arquivo de teste do arquivo api_cnpj_service.py.


# Como executar o projeto
Após instalar as bibliotecas necessarias

```bash
# clonar repositório
git clone https://github.com/Andreivilla/cnpj_data

# executar o projeto
get_company_data cnpj

# executar teste da api
python -m unittest service_test.py	
```

# Autor

Andrei Antonio Villa

https://github.com/Andreivilla
