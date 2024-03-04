import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_txt = txt_importer(path_file)

    if not isinstance(file_txt, list):
        return None

    dict_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_txt),
        "linhas_do_arquivo": file_txt,
    }

    if instance.__len__() > 0:
        for i in range(instance.__len__()):
            if (
                instance.search(i)["nome_do_arquivo"]
                == dict_file["nome_do_arquivo"]
            ):
                return None

    instance.enqueue(dict_file)
    sys.stdout.write(str(dict_file))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
