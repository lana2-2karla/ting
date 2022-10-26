import sys
import os


def txt_importer(path_file: str):
    if not os.path.isfile(path_file):
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    if path_file.endswith('.txt'):
        with open(path_file, 'r') as file:
            file = file.read().split("\n")
        return file
    return sys.stderr.write("Formato inválido\n")
