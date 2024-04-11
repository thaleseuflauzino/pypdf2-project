import os
from PyPDF2 import PdfReader
from datetime import datetime

def extrair_texto_e_metadados(pdf_path):
    texto = ''
    metadados = {}

    with open(pdf_path, 'rb') as pdf_file:
        reader = PdfReader(pdf_file)
        
        # Extrair texto
        qtdpage = input("Digite o tanto de páginas que deseja extrair: (0 para tudo)")
        qtdpage = int(qtdpage)
        for page_num in range(len(reader.pages)):
            if qtdpage == 0:
                page = reader.pages[page_num]
                texto += page.extract_text()
            if page_num <= qtdpage:
                page = reader.pages[page_num]
                texto += page.extract_text()

        # Extrair metadados
        metadados = reader.metadata

    return texto, metadados

def salvar_em_txt(texto, txt_path):
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(texto)

def excluir_pdf(pdf_path):
    os.remove(pdf_path)

def main():
    # Caminho do PDF
    pdf = input("escreva o nome do arquivo: ")
    pdf_path = pdf + ".pdf"
    
    # Extrair texto e metadados
    texto, metadados = extrair_texto_e_metadados(pdf_path)
    
    # Imprimir texto e metadados
    print('Texto extraído do PDF:')
    print(texto)
    print('\nMetadados do PDF:')
    print(metadados)
    
    # Salvar o texto extraído em um arquivo de texto
    txt_path = 'texto_extraido.txt'
    salvar_em_txt(texto, txt_path)
    print(f'\nTexto extraído salvo em "{txt_path}"')
    

    # Imprimir metadados específicos
    for key in metadados.keys():
        if key == "/CreationDate":
            data_string = metadados[key]
            data_limpa = data_string.split("D:")[1].split("-")[0]
            data = datetime.strptime(data_limpa, "%Y%m%d%H%M%S")
            data_formatada = data.strftime("%d/%m/%y")
            print("Data formatada:", data_formatada)

    
    # Excluir o arquivo PDF
    # excluir_pdf(pdf_path)
    # print(f'\nPDF "{pdf_path}" excluído com sucesso.')


if __name__ == "__main__":
    main()