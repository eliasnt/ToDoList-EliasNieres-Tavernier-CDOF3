import os

inp=5
comp=0
tasks=[]
while(inp!=4):
    
    print("Welcome to your to todolist : ")
    a=1
    for i in tasks:
        print(f"{a}. {i}")
        a+=1
    print(f"You have completed {comp} tasks")
        

    print("What do you want to do ? \n1.Add a new task \n2.Delete a task \n3.Complete a task \nTo leave enter any other keys")
    input1=input()
    if(input1=="1"):
        print("Enter the task to add")
        tasks.append(input())
        os.system('cls')
    elif(input1=="2"):
        if tasks:
            print("Choose the task to delete")
            entry=input()
            if(entry.isnumeric):
                entry=int(entry)
                if 0 < entry <= len(tasks):
                    tasks.pop(entry - 1)
                else:
                    os.system('cls')
                    print("impossible de remove")
            else:
                os.system('cls')
                print("impossible to remove")
        else:
            os.system('cls')
            print("The list is empty you can't remove anything")
    elif(input1=="3"):
        if tasks:
            print("Which task have you completed")
            entry=input()
            if(entry.isnumeric):
                entry=int(entry)
                if 0 < entry <= len(tasks):
                    os.system('cls')
                    tasks.pop(entry - 1)
                    comp=comp+1
                else:
                    os.system('cls')
                    print("impossible de remove")

            else:
                os.system('cls')
                print("the task doesnt exist")
        else:
            os.system('cls')
            print("The list is empty there is nothing to complete")
    else:
        inp=4