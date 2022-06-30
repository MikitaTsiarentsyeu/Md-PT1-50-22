import json


with open('dictionary.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


def get_all_content():
    return data


def add_new(word, translate, context=None, type_w=None):
    new_word = [word, translate, context, type_w]
    for id in range(1, len(data) + 2):
        if str(id) not in data:
            data[id] = {'Word': word,
                        'Translate': translate,
                        'Context': context,
                        'Type': type_w
                        }

            with open('dictionary.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            return True
    return False


def delete_word_name(word):
    for key in data:
        if word == data[key]['Word'] or word.lower() == data[key]['Word'].lower():  # if user entered an incorrect register:
            del data[key]
            with open('dictionary.json', 'w', encoding='utf-8') as file:
                json.dump(data, file,  ensure_ascii=False, indent=4)
            return True
    return False


def delete_word_id(word_id):
    if word_id in data:
        del data[word_id]
        with open('dictionary.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            return True
    return False


def edit_word(word_id, key, value, ):
    try:
        word = data[word_id]
        for i in word:
            if i.lower() == key.lower():  # if user entered an incorrect register:
                word[i] = value.title()
                with open('dictionary.json', 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
                return True
    except KeyError:
        return False
