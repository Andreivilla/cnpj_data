from company import company
import sys
from pdf_maker import pdf_maker

#atravez do paramtro 1 do terminal cria um objeto company
if len(sys.argv) != 2:
    raise ValueError("Um parâmetro é necessário.")

cnpj = sys.argv[1]
company = company(cnpj)
data_company = company.data_json()#adciona a essa variavel dados da empresa no padrão json


for dado in data_company:
    #lista object
    if dado in ['atividade_principal', 'atividades_secundarias', 'qsa']:
        print(dado + ': ')
        for dict in data_company.get(dado):
            for item in dict:
                print('   ' + item + ' : ' + dict.get(item))
    else:
    #no object
        print(dado + ': ' + str(data_company.get(dado)))

if (data_company.get('status') != 'ERROR'):
    pdf = pdf_maker(data_company)
    pdf.make_pdf()