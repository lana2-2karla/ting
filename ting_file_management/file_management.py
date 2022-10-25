import sys
import os

def txt_importer(path_file: str):
    if os.path.isfile(path_file) == False:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    if path_file.endswith('.txt'):
        with open(path_file,'r') as file:
         file = file.read().split("\n")
         print(file)
         return file
    return sys.stderr.write(f"Formato inválido\n")


# ref os: https://wallacemaxters.com.br/blog/72/como-verificar-se-um-arquivo-ou-diretorio-existe-em-python#:~:text=Em%20Python%2C%20o%20m%C3%A9todo%20os,tamb%C3%A9m%20%C3%A9%20um%20arquivo%20regular.
# ref erros com sys: https://codare.aurelio.net/2007/01/30/python-imprimir-mensagens-de-erro-stderr/#:~:text=write(%22ERRO%3A%20mensagem%20de,de%20qualquer%20tipo%20de%20arquivo.