class Node:                #Node
  id=1
  # constructor
  def __init__(self, data = None, next=None, status=None): 
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
            # List.incompleteTask()
            pass 
        elif task == 'Search Task':   #Hitesh
            # List.searchTask()
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
            List.head = temp.next
            flag = 1
    if flag == 0:
        while(temp is not None):
            if temp.data == task_string or temp.id == task_number:
                break
            prev = temp
            temp = temp.next       
    if(temp == None):
            return
    prev.next = temp.next
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
    pass

def SearchTask(self, value):
        curr = self.head
        f = open("outputPS5.txt", "a")
        str1 = "SEARCHED:book"
        str2 = "--------------------------------"
        f.write(str1)
        f.write(str2)
        while (curr != None):
            actionid, Lvalue = curr.data.split("-")
            if value.upper() in Lvalue.upper():
                f.write(curr.data)
            curr = curr.next
        f.write(str2)
        f.close()
        


 
initiateToDoList("inputPS5.txt")
   



