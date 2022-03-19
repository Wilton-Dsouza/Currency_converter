class Node:                #Node
  id=1
  # constructor
  def __init__(self, data = None, next=None, status='I'): 
    self.data = data
    self.next = next
    self.status = status
    self.id = Node.id
    Node.id += 1

class LinkedList:            #List
  def __init__(self):  
    self.head = None
    self.last_node = None

List = LinkedList()
def initiateToDoList(input_file):
    fp = open(input_file, "r")
    while True:
        lines = fp.readline()
        if lines == "":
            break
        task,action = lines.split(":")
        #print(task,action)
        if task == 'Add a Task':        #Upendra done
            addTask(action)
        elif task == 'Remove Task':     #Upendra done
            removeTask(action)
        elif task == 'Mark Complete':  #Wilton done
            completeTask(action)
            pass
        elif task == 'Mark InComplete': #Vishak
            # List.incompleteTask()
            pass 
        elif task == 'Task Status':   #Hitesh
            statusTask()
            pass 
        elif task == 'Search Task':   #Hitesh
            searchTask(action)
            pass
    fp.close()

def addTask(task_string):
    if List.last_node is None:
            List.head = Node(task_string)
            List.last_node = List.head
    else:
            List.last_node.next = Node(task_string)
            List.last_node = List.last_node.next
    f = open("outputPS5.txt", "a")
    str1 = "ADDED:TA"+str(List.last_node.id)+"-"+str(List.last_node.data.lstrip())
    f.write(str1)
    f.close()
    return
    
def removeTask(task_string = None, task_number = None):
    res = True if next((chr for chr in task_string if chr.isdigit()), None) else False
    if res is True:
        task_number = int(''.join(filter(lambda i: i.isdigit(), task_string)))
    temp = List.head
    flag = 0
    
    if (temp is not None):
        if (temp.data == task_string or temp.id == task_number):
            List.head = List.head.next
            flag = 1

    if flag == 0:
        while(temp is not None):
            if temp.data == task_string or temp.id == task_number:
                prev.next = temp.next
                break
            prev = temp
            temp = temp.next       
    if(temp == None):
            return 
    f = open("outputPS5.txt", "a")
    str1 = "REMOVED:TA"+str(temp.id)+"-"+str(temp.data.lstrip())
    f.write(str1)
    f.close()
    temp = None

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

def searchTask(search_string):
        value = search_string.replace(".","").strip()
        curr = List.head
        str1 = "SEARCHED:"+search_string
        str2 = "----------------------\n"
        f = open("outputPS5.txt", "a")
        f.write(str1)
        f.write(str2)
        while curr:
            Lvalue = curr.data
            if value.upper() in Lvalue.upper():
                f.write(curr.data)
            curr = curr.next
        f.write(str2)
        f.close()
       
def  statusTask():
        curr = List.head
        str1 = 'TASK-STATUS:\n'
        str2 = 'Task-Number Task-String     Task-Status\n'
        str3 = "--------------------------------\n"
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
        
 
initiateToDoList("inputPS5.txt")
   



