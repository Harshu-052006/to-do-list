todo=[]

def add():
    print("Add what to do")
    try:
        n=int(input("Enter the number of task:"))

    except:
        print("Please enter the valid input only numbers")
        return
    for i in range(n):
        task=input(f"{i+1}. ")
        todo.append(task)
    print("Adding Task plz wait")
    print("Added Task Succesfully")


def dlt():
    if not todo:
        print("There is nothing to delete")
        return
    
    view()
    print("Choose which number of task to Delete")
    try:
        n=int(input("Enter the number of task:"))
        del todo[n-1]   
        print("Deleting Task plz wait")
        print("Task Deleted")
    except ValueError:
        print("Invalid input! Please enter number.")
    except IndexError:
        print("That entered number in not there.")
    view()


def view():
    print("-"*20)
    print("     To Do List")
    print("-"*20)
    if not todo:
        print("   (No task found)")
    else:
        for index,task in enumerate(todo):
            print(f"{index + 1}.{task}")

def good_bye():
    print("Good bye!")