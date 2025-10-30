# Project:
#  Simple To-Do List. Create a program that allows a user to manage a to-do list. The user should be able to:
#  Add a new task.
#  View all tasks.
#  Delete a task by its name or number.
#  The program should loop until the user decides to quit.
print("Hello To-Do list")
todo = []
while True:

    print("Hello To-Do list")
    for loop, tasks in enumerate(todo , 1):
        print(f"{loop}.{tasks}")

    besh = input("\n\nYour next action is : \n1.Add a new task. \n2.View all tasks.\n3.Delete a task.\n4.Quit \n :")


    if besh == '1' and "Add a new task":
        task = input("Enter new task: ")

        todo.append(task)
    elif besh == '2' and "View all tasks":
        print("here is your tasks:")
        for loop, tasks in enumerate(todo, 1):
            print(f"{loop}.{tasks}")

    elif besh == '3' and "Delete a task":
        task_del = int(input("Enter task to delete: "))
        if 0 < task_del <= len(todo):
            todo.pop(task_del-1)
            print ("you have deleted %d" % task_del)
    elif besh == '4' and "Quit":
        break
    else :
        print (" There is something wrong")


