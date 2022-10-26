from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    list_text = txt_importer(path_file)
    info_text = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(list_text),
        "linhas_do_arquivo": list_text,
    }
    instance.enqueue(info_text)
    return sys.stdout.write(f"{info_text}\n")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
