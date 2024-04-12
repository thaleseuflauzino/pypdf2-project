import os
from PyPDF2 import PdfReader
from datetime import datetime, timedelta

def extrair_texto_e_metadados(pdf_path):
    texto = ''
    metadados = {}

    with open(pdf_path, 'rb') as pdf_file:
        reader = PdfReader(pdf_file)
        
        while True:
            qtdpage = input("\nDigite o tanto de páginas que deseja extrair:\n 0 to stop\n 'all' for all pages\n")
            if qtdpage.lower() == 'all':
                qtdpage = len(reader.pages)
                break
            if qtdpage.isdigit():
                qtdpage = int(qtdpage)
                break
            else:
                print("\nDigite um número inteiro valido\n")

        for page_num in range(len(reader.pages)):
            if qtdpage == 0:
                break
            if page_num < qtdpage:
                page = reader.pages[page_num]
                texto += page.extract_text()
        if qtdpage != 0: 
            metadados = reader.metadata

    return texto, metadados

def salvar_em_txt(texto, txt_path):
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(texto)

def excluir_pdf(pdf_path):
    os.remove(pdf_path)

def main():
    pdf = input("escreva o nome do arquivo: ")
    pdf_path = pdf + ".pdf"
    
    texto, metadados = extrair_texto_e_metadados(pdf_path)
    
    if(texto != '' and metadados != {}):
        print('Texto extraído do PDF:')
        print(texto)
        print('\nMetadados do PDF:')
        print(metadados)

        txt_path = 'texto_extraido.txt'
        salvar_em_txt(texto, txt_path)
        print(f'\nTexto extraído salvo em "{txt_path}"')
    

    for key in metadados.keys():
        if key == "/CreationDate":
            data_string = metadados[key]
            data_limpa = data_string.split("D:")[1].split("-")[0]
            data = datetime.strptime(data_limpa, "%Y%m%d%H%M%S") + timedelta(days = 1) # adiciona 1 dia
            data_formatada = data.strftime("%d/%m/%y")
            print("Data formatada:", data_formatada)

    
    # apaga o pdf
    # excluir_pdf(pdf_path)
    # print(f'\nPDF "{pdf_path}" excluído com sucesso.')


if __name__ == "__main__":
    main()