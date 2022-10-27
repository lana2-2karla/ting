from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):

    ocorrencias_info = []

    for index, text in enumerate(instance._data):
        if word.lower() in text['linhas_do_arquivo'].lower():
            dict_info_text = {
                "palavra": word,
                "arquivo": text["nome_do_arquivo"],
                "ocorrencias": [{f"linha: {index + 1}"}]
            }
            dict_info_text.append(ocorrencias_info)
    return ocorrencias_info


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
