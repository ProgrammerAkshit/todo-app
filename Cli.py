import time

from function import get_todos, write_todos

now = time.strftime("%b %d, %Y %H:%M:%S")

print("It is" , now)

while True:
    user_action = input("Type add , show, edit, completed or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo.capitalize() + "\n")

        write_todos(filepath = "todos.txt" , todos_arg= todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo.capitalize() + '\n'

            write_todos(filepath = "todos.txt" , todos_arg= todos)
        except ValueError:
            print("You enter wrong command!...")
            continue

    elif user_action.startswith('completed'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(filepath = "todos.txt" , todos_arg= todos)

            message = f"Todo {todo_to_remove} was removed from the list."

            print(message)
        except IndexError:
            print("The item you mentioned is not in the list!")
            continue

    elif 'exit' in user_action:
        break
    else:
        print("You entered wrong command!...... Type again")
print('Bye')



