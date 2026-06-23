import time

todo=[]

def add():
    print("Add what to do")
    n=int(input("Enter the number of task:"))
    for i in range(n):
        task=input(f"{i+1}. ")
        todo.append(task)
    print("Adding Task plz wait")
    time.sleep(2)
    print("Added Task Succesfully")


def dlt():
    print(todo)
    print("Choose which number of task to Delete")
    n=int(input("Enter the number of task:"))
    del todo[n-1]   
    print("Deleting Task plz wait")
    time.sleep(2)
    print("Task Deleted")
    print(todo)


def view():
    print("-"*20)
    print("     To Do List")
    print("-"*20)
    for index,task in enumerate(todo):
        print(f"{index + 1}.{task}")

def good_bye():
    print("Good bye!")

