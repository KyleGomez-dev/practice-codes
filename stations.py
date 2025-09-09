
class Node:
    def __init__(self, station):
        self.station = station
        self.next = None
        
class Station:
    def __init__(self):
        self.head = None
        self.size = 1
    
    def addStation(self, station):  # ✅ accept station as parameter
        new_node = Node(station)
        if self.head is None:  # If list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse until last node
            current = current.next
        current.next = new_node
        self.size += 1
        
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
                return current.station
            current = current.next
        return print("station not found!")
        
    def distance(self, elem1, elem2):
            # Find positions of both elements
            index1, index2 = -1, -1
            index = 0
            current = self.head
    
            while current:
                if current.station == elem1:
                    index1 = index
                if current.station == elem2:
                    index2 = index
                current = current.next
                index += 1
    
            # If one of them not found
            if index1 == -1 or index2 == -1:
                raise ValueError("One or both elements not found in the list")
    
            # Return absolute distance
            return abs(index1 - index2)
    
    def length(self):
        return self.size
    
    def insert(self, data, position):
        new_node = Node(data)
        self.size += 1
        # Case 1: Insert at the head (position 0)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            
            return

        # Traverse to the node before the target position
        current = self.head
        index = 1
        while current and index < position:
            current = current.next
            index += 1

        if not current:  # position out of range
            raise IndexError("Position out of range")

        # Insert new node
        new_node.next = current.next
        current.next = new_node
    
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
    lenUpd = s.length()
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
        if lenUpd >= 3:
            add = input("Enter Station: ")
            if add.lower() == "stop":
                print("stop detected, stopping the function")
                continue
            else:
                s.display()
                location = int(input("Enter the position you want to insert the new station: "))
                s.insert(add,location)
                print(add,"is Added")
        else:
            add = input("Enter Station: ")
            if add.lower() == "stop":
                print("stop detected, stopping the function")
                continue
            elif add != "":
                s.addStation(add)
                print(add.title(), "Successfully added.")
            else:
                print("invalid station")
    elif userInput.lower() == "deletestation":
        toDelete = input("enter the station: ").lower()
        print(toDelete)
        if toDelete == s.search(toDelete):
            print(s.search(toDelete),"is successfully deleted.")
            s.delete(toDelete)
            lenUpd -= 1
    
    elif userInput.lower() == "getdistance":
        station1 = input("enter the first station: ").lower()
        station2 = input("enter the second station: ").lower()
        print(s.distance(station1, station2))
    elif userInput.lower() == "exit":
        print("exit detected, terminating the program.")
        break


            
            
            
            
            
            
            
    
            
        
        
        
        
        
