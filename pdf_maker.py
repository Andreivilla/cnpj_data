from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
import re

class pdf_maker:
    
    def __init__(self, data):
        self.data = data

    def mm_to_p(self, mm):
        return  mm /0.352777

    def make_string(self):#cria uma string formatada para o pdf
        txt = ''
        for dado in self.data:
        #lista object
            if dado in ['atividade_principal', 'atividades_secundarias', 'qsa']:
                txt += '<b>' + dado + '</b>' + ':<br/>'
                #print(txt)
                for dict in self.data.get(dado):
                    for item in dict:
                        txt += '-->' + item + ': ' + dict.get(item) + '<br/>'
            else:
            #no object
                txt += '<b>' + dado + '</b>: ' + str(self.data.get(dado)) + '<br/>'
        return txt
    
    def make_pdf(self):
        txt = self.make_string()

        # Cria um objeto de estilo
        styles = getSampleStyleSheet()

        # Define o estilo do parágrafo
        style_para = styles["Normal"]
        
        # Cria um objeto Paragraph
        para = Paragraph(txt, style_para)

        # Cria um objeto SimpleDocTemplate
        name = self.data.get('nome')
        pdf_name = "company" + name + ".pdf"
        doc = SimpleDocTemplate(pdf_name)

        # Adiciona o objeto Paragraph ao conteúdo do PDF
        content = [para]
        doc.build(content)