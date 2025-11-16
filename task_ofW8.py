# Project:
# Modify your To-Do List program from earlier. When the program starts,
# it should read any existing tasks from a file named tasks.txt.
# When the user adds or deletes a task, the program should update the file.
# This way, the tasks are not lost when the program closes.

#lets start to dividing tasks to each that we can work on
print("Hello To-Do list")
todo = []
while True:

    print("Hello To-Do list")
    for loop, tasks in enumerate(todo , 1):
        print(f"{loop}.{tasks}")

    besh = input("\n\nYour next action is : \n1.Add a new task. \n2.View all tasks.\n3.Delete a task.\n4.Quit \n :")


    if besh == '1' and "Add a new task":
        task = input("Enter new task: ")

        file = open("tasks.txt","a")
        file.write(f"{task}\n")
        file.close()

         # todo.append(task)

        # so first this we can use append for file
    elif besh == '2' and "View all tasks":
        # print("here is your tasks:")
        # for loop, tasks in enumerate(todo, 1):
        #     print(f"{loop}.{tasks}")
        # file = open("tasks.txt", "r")
        # for line in file:
        #     print(line)
        file = open("tasks.txt","r")
        print(file.read())
        file.close()


        # for second is good to use "r" mode just view
    elif besh == '3' and "Delete a task":
        task_del = int(input("Enter task to delete: "))
        if 0 < task_del <= len(todo):
            todo.pop(task_del-1)
            print ("you have deleted %d" % task_del)

        # this one is only delete the task
    elif besh == '4' and "Quit":
        break
    else :
        print (" There is something wrong")
