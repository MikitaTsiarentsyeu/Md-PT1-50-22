import data


def get_all_content():
    content = data.get_all_content()
    for i in content:
        print(f'{i}.')
        for key, value in content[i].items():
            if value is None:      # hide content
                continue
            print(f'    {key} - {value}')


def add_new_word(word:str, translate:str, context=None, type_w=None):
    if word and translate:
        if data.add_new(word=word.title(), translate=translate.title(), context=context, type_w=type_w):
            return True
    return False


def bl_edit_word(word_id, key, value):
    if data.edit_word(word_id, key, value):
        return True
    return False


def bl_delete_word(value):
    if not value.isdigit():
        if data.delete_word_name(value):
            return True
        return False
    else:
        if data.delete_word_id(value):
            return True
        return False