def exists_word(word, instance):
    lower_word = word.lower()
    result = []

    for file_index in range(len(instance)):
        file = instance.search(file_index)
        words = file["linhas_do_arquivo"]
        occurrences = [
            {"linha": line_index + 1}
            for line_index, line in enumerate(words)
            if lower_word in line.lower()
        ]

        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
