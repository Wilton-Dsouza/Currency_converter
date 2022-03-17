class Node:                #Node
  id=0
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next
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
        if task == 'Add a Task':        #Upendra
            addTask(action)
        elif task == 'Remove Task':     #Upendra
            removeTask(action)
        elif task == 'Mark Complete':  #Vishak
            # List.completeTask()
            pass
        elif task == 'Mark InComplete': #Wilton
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
    f = open("output.txt", "a")
    str1 = "ADDED:TA"+str(List.last_node.id)+"-"+str(List.last_node.data)
    f.write(str1)
    f.close()
    return
  
def SearchTask(self, value):
        curr = self.head
        f = open("output.txt", "a")
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
        
def removeTask(task_string):
    temp = List.head
    flag = 0
    
    if (temp is not None):
        if (temp.data == task_string):
            List.head = temp.next
            flag = 1
    if flag == 0:
        while(temp is not None):
            if temp.data.strip() == task_string.strip():
                break
            prev = temp
            temp = temp.next       
    if(temp == None):
            return
    prev.next = temp.next
    f = open("output.txt", "a")
    str1 = "REMOVED:TA"+str(temp.id)+"-"+str(temp.data)
    f.write(str1)
    f.close()
    temp = None

 
initiateToDoList("demofile.txt")
   



