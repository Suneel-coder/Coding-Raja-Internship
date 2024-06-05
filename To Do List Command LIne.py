def add_task(tasks):
    task_name=input("Enter the Task to be done: ")
    priority=input("Enter the priority like (high/medium/low): ")
    due_date=input("Enter the Due date DD-MM-YYYY: ")
    tasks.append({"Name":task_name,"Priority":priority,"Due Date":due_date,"Completed":False})
    print("Task Has been added Successfully")

def remove_task(tasks):
    print("Select the task from below that should be removed")
    for i,task in enumerate(tasks):
        print(f"{i+1}.{task['Name']}") 
    choice=int(input("Enter the Number corresponding to the task name: "))
    del tasks[choice-1]
    print("Task has been successfully removed from the list")

def mark_completed(tasks):
    print("Select the task from below that should be marked completed: ")
    for i,task in enumerate(tasks):
        print(f"{i+1}.{task['Name']}")
    choice=int(input("Enter the number corresponding to the task name: "))
    tasks[choice-1]["Completed"]=True
    print("Task has been successfully marked as completed")


def list_tasks(tasks):
    print("All the tasks are listed below")
    for i,task in enumerate(tasks):
        if task["Completed"]:
            status="Completed"
        else:
            status="Pending"
        print(f"{i+1}. {task['Name']}-Priority:{task['Priority']}, Due Date: {task['Due Date']}, Status: {status}")



tasks=[]
while (True):
    print("To Do List")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark as Task Completed")
    print("4. List the Tasks")
    print("5. Exit")
    choice=int(input("Enter Your Choice from above"))
    if choice==1:
        add_task(tasks)
    elif choice==2:
        remove_task(tasks)
    elif choice==3:
        mark_completed(tasks)
    elif choice==4:
        list_tasks(tasks)
    elif choice==5:
        print("Thank you for using this application")
        print("Exiting the application")
        break
    else:
        print("Invalid Input")
        print("Please try again")


