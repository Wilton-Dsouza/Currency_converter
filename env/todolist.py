import time
class Node:                # Node class
  id=1
  def __init__(self, data = None, next=None, status='I'): 
    self.data = data
    self.next = next
    self.status = status
    self.id = Node.id
    Node.id += 1

class LinkedList:           # Linked List implementation
  def __init__(self):  
    self.head = None    

def initiateToDoList(input_file):
    # Reading the contents of the file which has tasks and action, depending on that appropriate
    # functions are called.
    fp = open(input_file, "r")
    f =open("outputPS5.txt", 'r+') 
    f.truncate(0)
    f.close()
    while True:
        lines = fp.readline()
        if lines == "":
            break
        task,action = lines.split(":")
        task = task.lower()
        if task == 'add a task':        
            addTask(action)
        elif task == 'remove task':     
            removeTask(action)
        elif task == 'mark complete':  
            completeTask(action)
        elif task == 'mark incomplete': 
            incompleteTask(action)
        elif task == 'task status':   
            statusTask()
        elif task == 'search task':   
            searchTask(action)
    fp.close()

def addTask(task_string):
    # If the List is empty, it adds a task at the beginning else it will iterate and append to the
    # last node
    f = open("outputPS5.txt", "a")
    task_string = task_string.replace(".","").strip()
    if List.head is None:
        List.head = Node(task_string)
        List.head.next = None
        str1 = "ADDED:TA"+str(List.head.id)+"-"+str(List.head.data.strip())+"\n"
    else:
        new_node = Node(task_string)
        last = List.head
        while (last.next):
            last = last.next
        last.next =  new_node
        str1 = "ADDED:TA"+str(last.next.id)+"-"+str(last.next.data.strip())+"\n"
    f.write(str1)
    f.close()
    
def removeTask(task_string = None, task_number = None):
    # This function removes all the nodes with same task
    flag2 = 0
    task_string = task_string.replace(".","").strip()
    value = task_string
    if task_string[2].isdigit() and task_string[:2] == "TA":
        res = True
    else:
        res = False
    if res is True:
        task_number = int(task_string[2:])
        task_string = ""
    temp = List.head
    temp = temp.next
    prev = List.head       
    f = open("outputPS5.txt", "a")
    while(temp is not None): # Removes the other nodes except the head node
        flag = 0
        if temp.data.upper() == task_string.upper() or temp.id == task_number:
            flag = 1
            flag2 = 1
            str1 = "REMOVED:TA"+str(temp.id)+"-"+str(temp.data.lstrip())+"\n"
            f.write(str1)
            prev.next= temp.next
            temp = prev.next
        if flag == 0:
            prev = temp
            temp = temp.next
    temp = List.head
    if (temp is not None): # Removes the head node
        if (temp.data.upper() == task_string.upper() or temp.id == task_number):
            flag2 = 1
            str1 = "REMOVED:TA"+str(temp.id)+"-"+str(temp.data.lstrip())+"\n"
            f.write(str1)
            List.head = temp.next
            prev = temp
    if flag2 == 0:
            f.write(value+" - to be removed not found\n")
    f.close()

def completeTask(task_string = None, task_number = None):
    # This function sets the status of the task to Complete i.e., C
    flag = 0
    task_string = task_string.replace(".","").strip()
    value = task_string
    if task_string[2].isdigit() and task_string[:2] == "TA":
        res = True
    else:
        res = False
    if res is True:
        task_number = int(task_string[2:])
        task_string = ""
    current = List.head
    f = open("outputPS5.txt", "a") 
    while current:
        if task_string.upper() == current.data.upper() or task_number == current.id:
            flag = 1
            str1 = "Completed:TA"+str(current.id)+"-"+str(current.data.lstrip())+"\n"
            current.status = "C"
            f.write(str1)
        current = current.next
    if flag == 0:
            f.write(value+" - to be marked complete is not found \n")
    f.close()


def incompleteTask(task_string = None, task_number = None):
    # This function sets the status of the task to InComplete i.e., I
    flag = 0
    task_string = task_string.replace(".","").strip()
    value = task_string
    if task_string[2].isdigit() and task_string[:2] == "TA":
        res = True
    else:
        res = False
    if res is True:
        task_number = int(task_string[2:])
        task_string = ""
    current = List.head
    f = open("outputPS5.txt", "a")
    while current:
        if task_string.upper() == current.data.upper() or task_number == current.id:
            flag = 1
            str1 = "UNCOMPLETED:TA"+str(current.id)+"-"+str(current.data.lstrip())+"\n"
            current.status = "I"
            f.write(str1)
        current = current.next
    if flag == 0:
        f.write(value+" - to be marked incomplete is not found \n")
    f.close()


def searchTask(search_string):
    # This function searches the task from the Linked List with the given search string
        flag = 0
        value = search_string.replace(".","").strip()
        curr = List.head
        str1 = "SEARCHED:"+search_string
        str2 = "-------------------------------\n"
        f = open("outputPS5.txt", "a")
        f.write(str1)
        f.write(str2) 
        while curr:
            Lvalue = curr.data
            if value.upper() in Lvalue.upper():
                flag = 1
                f.write("TA"+str(curr.id)+"-"+curr.data+"\n")
            curr = curr.next
        if flag == 0:
            f.write(value+" - task not found\n")
        f.write(str2)
        f.close()
       
def  statusTask():
    # This function displays the status of the to do activities
        curr = List.head
        str1 = 'TASK-STATUS:\n'
        str2 = 'Task-Number Task-String     Task-Status\n'
        str3 = "-------------------------------\n"
        f = open("outputPS5.txt", "a")
        f.write(str1)
        f.write(str2)
        f.write(str3)   
        while (curr!= None):
            Actionid = curr.id
            TString = curr.data
            TNumber = "TA"+str(Actionid)
            TStatus = curr.status
            entry = TNumber+'        '+ TString.rstrip()+'   '+TStatus+'\n'
            f.write(entry)
            curr = curr.next
        f.write(str3)
        f.close()

List = LinkedList()             
initiateToDoList("inputPS5.txt") # Function call and passing input file as parameter to the function
