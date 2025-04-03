'''
Arquivo: data_acquisition.py
Autor: André Rizzo

Módulo de aquisição de dados para o projeto de classificação de tomates.
Responsável por baixar e extrair o dataset do Kaggle.
'''

import os
import zipfile
import shutil
import gdown    

def download_and_extract_dataset(gdrive_url, download_path, extract_path):
    """
    Faz o download de um arquivo do GitHub (via URL raw) e, se for um ZIP, pode extrair seu conteúdo.

    Args:
        github_url (str): URL raw do arquivo no GitHub.
        download_path (str): Caminho do diretório onde o arquivo será salvo. 
        extract_path (str): Caminho onde o conteúdo do ZIP será extraído, se aplicável.

    Returns:
        None
    """

    # Cria diretório de download, se necessário
    os.makedirs(download_path, exist_ok=True)

    # Caminho completo do arquivo a ser salvo
    zip_file_path = os.path.join(download_path, "tomates_dataset.zip")

    # Baixa o arquivo
    print("Baixando dataset do Google Drive...")
    gdown.download(gdrive_url, output=zip_file_path, quiet=False)

    # Verifica se o arquivo foi baixado
    if os.path.exists(zip_file_path):
        print(f"Extraindo {zip_file_path}...")
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        print(f"Extração concluída em: {extract_path}")
    else:
        print("Erro: o arquivo não foi baixado corretamente.")



def organize_images(extract_path):
    """
    Organiza imagens extraídas de um dataset em novos diretórios com nomes em português, 
    
    A função realiza as seguintes etapas:
    1. Cria os diretórios de destino: 'Danificados', 'Verdes', 'Maduros' e 'Velhos'.
    2. Percorre recursivamente os diretórios extraídos do dataset.
    3. Identifica pastas com os nomes originais em inglês: 'Damaged', 'Unripe', 'Ripe' e 'Old'.
    4. Move os arquivos de imagem de cada pasta para seus respectivos diretórios com nome em português:
        - 'Damaged'  →  'Danificados'
        - 'Unripe'   →  'Verdes'
        - 'Ripe'     →  'Maduros'
        - 'Old'      →  'Velhos'

    Args:
        extract_path (str): Caminho base onde os dados foram extraídos e onde a reorganização será realizada.
      

    Requisitos:
            O caminho xtract_path deve conter as subpastas originais do dataset ('Damaged', 'Unripe', etc.).
            O script cria automaticamente os diretórios de destino, caso não existam.

    Retorno:
            None
    """
    

    # Composição dos nomes dos novos diretórios
    path_danificados = os.path.join(extract_path, 'Danificados')
    path_verdes = os.path.join(extract_path, 'Verdes')
    path_maduros = os.path.join(extract_path, 'Maduros')
    path_velhos = os.path.join(extract_path, 'Velhos')

    # Criação dos novos diretórios para onde as imagens serão movidas
    os.makedirs(path_danificados, exist_ok=True)
    print(f'Diretório {path_danificados} criado com sucesso')

    os.makedirs(path_verdes, exist_ok=True)
    print(f'Diretório {path_verdes} criado com sucesso')

    os.makedirs(path_maduros, exist_ok=True)
    print(f'Diretório {path_maduros} criado com sucesso')

    os.makedirs(path_velhos, exist_ok=True)
    print(f'Diretório {path_velhos} criado com sucesso')


    for root, folders, files in os.walk(extract_path):
        for dir in folders:
            if dir == 'Damaged':
                damaged_path = os.path.join(root, dir)
                
                for file in os.listdir(damaged_path):
                    file_path = os.path.join(damaged_path, file)
                    if os.path.isfile(file_path):
                        shutil.move(file_path, path_danificados)
                        print(f'Movido: {file_path}   →   {path_danificados}')

            elif dir == 'Unripe':
                unripe_path = os.path.join(root, dir)
                
                for file in os.listdir(unripe_path):
                    file_path = os.path.join(unripe_path, file)
                    if os.path.isfile(file_path):
                        shutil.move(file_path, path_verdes)
                        print(f'Movido: {file_path}   →   {path_verdes}')
            
            elif dir == 'Ripe':
                ripe_path = os.path.join(root, dir)
                
                for file in os.listdir(ripe_path):
                    file_path = os.path.join(ripe_path, file)
                    if os.path.isfile(file_path):
                        shutil.move(file_path, path_maduros)
                        print(f'Movido: {file_path}   →   {path_maduros}')
            
            elif dir == 'Old':
                old_path = os.path.join(root, dir)
                
                for file in os.listdir(old_path):
                    file_path = os.path.join(old_path, file)
                    if os.path.isfile(file_path):
                        shutil.move(file_path, path_velhos)
                        print(f'Movido: {file_path}   →   {path_velhos}')
    print('\nTodos os arquivos foram movidos com sucesso!')

    # Apaga os diretórios criados durante o unzip
    original_extracted_folder = os.path.join(extract_path, 'content')
    if os.path.exists(original_extracted_folder):
        shutil.rmtree(original_extracted_folder)
        print(f'\nPasta original "{original_extracted_folder}" removida com sucesso.')


