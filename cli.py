from functions import get_todos, write_todos
# import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")

print("The date and time is below: ", '\n')
print("It is", now, '\n')

while True:
    # get user input and strip space characters from it
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    # add a todo
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos("todos.txt")
        todos.append(todo + '\n')

        write_todos("todos.txt", todos)

    # show todos in the list
    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")

        for index, item in enumerate(todos, start=1):
            item = item.strip('\n')
            row = f"{index}.{item}"
            print(row)

    # editing a todo in the list
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos("todos.txt")

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos("todos.txt", todos)

        except ValueError:
            print("Your Command is not valid.")
            continue

    # check finish or complete in the todo
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos("todos.txt")

            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            write_todos("todos.txt", todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print("Your Command is not valid")
            continue

    # exit the todo list
    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")

print("Bye!")
