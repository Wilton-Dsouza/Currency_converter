class Node:                  #Node
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

class LinkedList:            #List
  def __init__(self):  
    self.head = None


def initiateToDoList(input_file):
    fp = open(input_file, "r")
    List = LinkedList()
    while True:
        lines = fp.readline()
        if lines == "":
            break
        task,action = lines.split(":")
        print(task,action)
        if task == 'Add a Task':        #Upendra
            pass
            # List.addTask(action)
        elif task == 'Remove Task':     #Upendra
            # List.removeTask()
            pass
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

initiateToDoList("demofile.txt")
   



