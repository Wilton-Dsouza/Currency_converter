import time
class Node:                
  id=1
  # constructor
  def __init__(self, data = None, next=None, status='I'): 
    self.data = data
    self.next = next
    self.status = status
    self.id = Node.id
    Node.id += 1

class LinkedList:            
  def __init__(self):  
    self.head = None

List = LinkedList()
def initiateToDoList(input_file):
    fp = open(input_file, "r")
    f =open("outputPS5.txt", 'r+') 
    f.truncate(0)
    f.close()
    
    while True:
        lines = fp.readline()
        if lines == "":
            break
        task,action = lines.split(":")
        if task == 'Add a Task':        
            addTask(action)
        elif task == 'Remove Task':     
            removeTask(action)
        elif task == 'Mark Complete':  
            completeTask(action)
        elif task == 'Mark InComplete': 
            incompleteTask(action)
        elif task == 'Task Status':   
            statusTask()
        elif task == 'Search Task':   
            searchTask(action)
    fp.close()

def addTask(task_string):
    f = open("outputPS5.txt", "a")
    if List.head is None:
        List.head = Node(task_string)
        List.head.next = None
        str1 = "ADDED:TA"+str(List.head.id)+"-"+str(List.head.data.lstrip())

    else:
        new_node = Node(task_string)
        last = List.head
        while (last.next):
            last = last.next
        last.next =  new_node
        str1 = "ADDED:TA"+str(last.next.id)+"-"+str(last.next.data.lstrip())
    f.write(str1)
    f.close()
    return
    
def removeTask(task_string = None, task_number = None):
    res = True if next((chr for chr in task_string if chr.isdigit()), None) else False
    if res is True:
        task_number = int(''.join(filter(lambda i: i.isdigit(), task_string)))
    temp = List.head
    f = open("outputPS5.txt", "a")
    if (temp is not None):
        if (temp.data == task_string or temp.id == task_number):
            str1 = "REMOVED:TA"+str(temp.id)+"-"+str(temp.data.lstrip())
            List.head = temp.next

    while(temp is not None):
        flag = 0
        if temp.data == task_string or temp.id == task_number:
            flag = 1
            str1 = "REMOVED:TA"+str(temp.id)+"-"+str(temp.data.lstrip())
            prev.next= temp.next
            temp = prev.next
        if flag == 0:
            prev = temp
            temp = temp.next


    f.write(str1)
    f.close()

def completeTask(task_string = None, task_number = None):
    res = True if next((chr for chr in task_string if chr.isdigit()), None) else False
    if res is True:
        task_number = int(''.join(filter(lambda i: i.isdigit(), task_string)))
    current = List.head
    while current:
        if task_string == current.data or task_number == current.id:
            f = open("outputPS5.txt", "a")
            str1 = "Completed:TA"+str(current.id)+"-"+str(current.data.lstrip())
            current.status = "C"
            f.write(str1)
            f.close()
        current = current.next

def incompleteTask(task_string = None, task_number = None):
    res = True if next((chr for chr in task_string if chr.isdigit()), None) else False
    if res is True:
        task_number = int(''.join(filter(lambda i: i.isdigit(), task_string)))
    current = List.head
    while current:
        if task_string == current.data or task_number == current.id:
            f = open("outputPS5.txt", "a")
            str1 = "UNCOMPLETED:TA"+str(current.id)+"-"+str(current.data.lstrip())
            current.status = "I"
            f.write(str1)
            f.close()
        current = current.next

def searchTask(search_string):
        flag = 0
        value = search_string.replace(".","").strip()
        curr = List.head
        str1 = "SEARCHED:"+search_string+"\n"
        str2 = "-------------------------------\n"
        f = open("outputPS5.txt", "a")
        f.write(str1)
        f.write(str2)
        while curr:
            Lvalue = curr.data
            if value.upper() in Lvalue.upper():
                flag = 1
                f.write(curr.data)
            curr = curr.next
        if flag == 0:
            f.write(value+" Not Found\n")
        f.write(str2)
        f.close()
       
def  statusTask():
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
        
start =time.time()
initiateToDoList("inputPS5.txt")
end = time.time()
print(end - start)
