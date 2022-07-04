import bl


def choose_option():
    while True:
        user_input = input('Hello, select an action to interact with the application\n'
                           'Press "1" to see all dictionary\n'
                           'Press "2" to add new word\n'
                           'Press "3" to edit word\n'
                           'Press "4" to delete word\n')
        if user_input == '1':
            view_content()
            break
        elif user_input == '2':
            add_new_word()
            break
        elif user_input == '3':
            user_edit_word()
            break
        elif user_input == '4':
            user_delete_word()
            break
        else:
            print('Oops, most likely you entered the option in the wrong format, please try again'
                  '\n')


def error_message():
    print("Oops, something went wrong...\n"
          "Most likely you entered value that doesn't exist or is incorrect. ")

def view_content():
    print('You have selected the option to view the contents of the dictionary.')
    return bl.get_all_content()

def add_new_word():
    print('You have selected the option to add a new word.')
    word = input("Please enter the word:\n")
    translate = input("Please enter the translation:\n")
    context = input("Please enter the context(Optional, leave the field empty if there is no context):\n")
    type_w = input("Please enter the type(Optional, leave the field empty if there is no context):\n")

    if bl.add_new_word(word, translate, context, type_w):
        return print('The word was been successfully added')
    return error_message()


def user_edit_word():
    print("You have selected the dictionary editing option. Please, enter the number of the word,"
          "the value you want to change and the new value.")
    word_id = input("Please enter the word number(you can look it up in the dictionary):\n")
    key = input('Please enter the value you want to change("Word", "Translate", "Context", "Type"):\n')
    value = input("Please enter the new value:\n")

    if bl.bl_edit_word(word_id=word_id, key=key, value=value):
        return print('The word has been correctly edited')
    return error_message()

def user_delete_word():
    print("You have selected the option to remove the word from the dictionary.")
    value = input("Please enter the word or word number you want to remove from the dictionary:\n")
    if value:
        if bl.bl_delete_word(value):
            return print('The word has been correctly deleted')
        return error_message()
    else:
        print("The field must not be empty. Please enter a value")
        print("Let's try again...\n")
        user_delete_word()


