FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ function to read and return the to-dos

    :param filepath: file name with its path from which we are reading the to-dos
    :return: it returns the to-dos read from the file
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()

    return todos_local


def write_todos(new_todos, filepath=FILEPATH):
    """function to write to-dos in a file

    :param filepath: file name with its path in which we are writing the to-dos
    :param new_todos:
    :return: it writes the to-dos read to the file
    """
    with open(filepath,'w') as file:
        file.writelines(new_todos)


print(__name__)
if __name__ == '__main__':
    print(help(get_todos))