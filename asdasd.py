class Node:
    def __init__(self, station):
        self.station = station
        self.next = None
        
class Station:
    def __init__(self):
        self.head = None
    
    def addStation(self, station):  # ✅ accept station as parameter
        new_node = Node(station)
        if self.head is None:  # If list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse until last node
            current = current.next
        current.next = new_node
        
    def delete(self, target):
        current = self.head

        # Case 1: target is the head
        if current and current.station == target:
            self.head = current.next  # move head
            current = None
            return True

        # Case 2: target is in middle or end
        prev = None
        while current:
            if current.station == target:
                prev.next = current.next
                current = None
                return True
            prev = current
            current = current.next

        # Case 3: not found
        return False
    
    def search(self, target):
        current = self.head
        while current:
            if current.station == target:   # ✅ check match
                return True
            current = current.next
        return False
    
    def display(self):
        current = self.head
        i = 1
        while current:
            print(f"[{i}]",current.station)  # ✅ use .station not .data
            current = current.next
            i += 1
            #### ✅ fixed output


# Example usage
s = Station()

print("Help             -   Show this menu")
print("printAllstations -   Show all stations")
print("addnewstation    -   add a new station")
print("deletestation    -   delete a station")
print("getdistance      -   measure the distance between two stations")
print("stop             -   stop current run")
print("exit             -   exit the program completely")
print()
print()
while True: 
    userInput = input("choose action: ")
    if userInput.lower() == "help":
        print("Help             -   Show this menu")
        print("printAllstations -   Show all stations")
        print("addnewstation    -   add a new station")
        print("deletestation    -   delete a station")
        print("getdistance      -   measure the distance between two stations")
        print("stop             -   stop current run")
        print("exit             -   exit the program completely")
        print()
        print()
    elif userInput.lower() == "printallstations":
        s.display()
    elif userInput.lower() == "addnewstation":
        add = input("Enter Station: ")
        if add != "":
            s.addStation(add)
            print(add.title(), "Successfully added.")
        else:
            print("invalid station")
    elif userInput.lower() == "deletestation":
        toDelete = input("enter the station: ")
        if toDelete.title() == s.search(toDelete):
            print(s.search(toDelete),"is successfully deleted.")
            s.delete(toDelete)
            
            
            
            
            
            
            
    
            
        
        
        
        
        

