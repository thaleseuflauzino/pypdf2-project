# Métodos de Desenvolvimento de Software
Este repositório é destinado para armazenar um miniprojeto sobre como utilizar a biblioteca PyPDF2.


### PDF Extractor

Este script permite extrair texto e metadados de um arquivo PDF e salvá-los em um arquivo de texto (.txt).

Pré-requisitos:
- Python 3.x
- PyPDF2 (instalável via pip: pip install PyPDF2)

Funcionalidades:
- Extrai texto e metadados de um PDF.
- Salva o texto extraído em um arquivo de texto.
- Formata a data de criação do PDF.
- Exclui o PDF após a extração (comentado por padrão).

Autor: Thales Henrique Euflauzino dos Santos
Data de Criação: 12/04/2024

Instruções de Uso:
1. Execute o script e forneça o nome do arquivo PDF quando solicitado.
2. Escolha a quantidade de páginas a extrair ou digite 'all' para todas as páginas.
3. O texto extraído será exibido no console e salvo em um arquivo de texto.
4. Os metadados, incluindo data de criação, título e autor, serão exibidos no console.

Nota: O PDF original será excluído após a extração (comentado por padrão). Descomente a linha relevante para ativar essa funcionalidade.
