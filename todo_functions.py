def get_todos(filepath='todos.txt'):
    """ Read a file and return the list of todo items. """
    with open(filepath, 'r') as file_local:
        todos = file_local.readlines()
    return todos

def write_todos(todos_arg, filepath='todos.txt'):
    """ Write a list of todo items to a specified file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)