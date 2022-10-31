from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):

    ocorrencias_info = []
    for item in range(len(instance)):
        file = instance.search(item)
        dict_info_text = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": []
        }
        for index, text in enumerate(file['linhas_do_arquivo']):
            if word.lower() in text.lower():
                dict_info_text['ocorrencias'].append({"linha": index + 1})
        if dict_info_text["ocorrencias"]:
            ocorrencias_info.append(dict_info_text)
    return ocorrencias_info


def search_by_word(word: str, instance: Queue):
    ocorrencias_info = []
    for item in range(len(instance)):
        file = instance.search(item)
        dict_info_text = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": []
        }
        for index, text in enumerate(file['linhas_do_arquivo']):
            if word.lower() in text.lower():
                dict_info_text['ocorrencias'].append({
                    "linha": index + 1,
                    "conteudo": text
                })
        if dict_info_text["ocorrencias"]:
            ocorrencias_info.append(dict_info_text)
    return ocorrencias_info
