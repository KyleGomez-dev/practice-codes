
class Node:
    def __init__(self, station):
        self.station = station
        self.next = None
        
class Station:
    def __init__(self):
        self.head = None
        self.size = 1

# ADD STATION
    def addStation(self, station): 
        new_node = Node(station)
        if self.head is None:  # If list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # loops until last node
            current = current.next
        current.next = new_node
        self.size += 1
# HELP
    def help(self): 
        print("""Available Commands:
          Help             -   Show this menu
          printAllstations -   Show all stations
          addnewstation    -   add a new station
          deletestation    -   delete a station
          getdistance      -   measure the distance between two stations
          stop             -   stop current run
          exit             -   exit the program completely""")
# DELETE STATION    
    def deleteStation(self, target):
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
#TO SEARCH A STATION
    def search(self, target):
        current = self.head
        while current:
            if current.station == target:   # search match
                return current.station
            current = current.next
        return print("station not found!")
#GET DISTANCE
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
#GETTING THE LENGTH OF LIST
    def length(self):
        return self.size
        
# ADDDING ELEMENT TO A SPECIFIC LOCATION
    def insert(self, data, position):
        new_node = Node(data)
        self.size += 1
        
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        index = 1
        while current and index < position:
            current = current.next
            index += 1

        if not current:  #if position out of range
            raise IndexError("Position out of range")

        # Insert new node
        new_node.next = current.next
        current.next = new_node
#PRINT ALL STATIONS
    def display(self):
        current = self.head
        i = 1
        while current:
            print(f"[{i}]",current.station) 
            current = current.next
            i += 1
            
            
#START OF THE PROGRAM
def Start():
    s = Station()
    
    print("""Available Commands:
          Help             -   Show this menu
          printAllstations -   Show all stations
          addnewstation    -   add a new station
          deletestation    -   delete a station
          getdistance      -   measure the distance between two stations
          stop             -   stop current run
          exit             -   exit the program completely""")
    print()
    print()
    
    while True: 
        lenUpd = s.length()
        userInput = input("choose action: ")
#HELP
        if userInput.lower() == "help":
            s.help()
            print()
            print()
#PRINT ALL STATIONS
        elif userInput.lower() == "printallstations":
            s.display()
#ADD NEW STATION
        elif userInput.lower() == "addnewstation":
            if lenUpd >= 3:
                add = input("Enter Station: ").title()
                if add == "Stop":
                    print("stop detected, stopping the current function")
                    continue
                else:
                    s.display()
                    location = input("Enter the position you want to insert the new station: ")
                    if location.lower == "stop":
                        print("stop detected, stopping the current function")
                        continue
                    else:
                        s.insert(add,location)
                        print(add,"is Added")
            else:
                add = input("Enter Station: ").title()
                if add == "Stop":
                    print("stop detected, stopping the current function")
                    continue
                elif add != "":
                    s.addStation(add)
                    print(add.title(), "Successfully added.")
                else:
                    print("invalid station")
#DELETE STATION
        elif userInput.lower() == "deletestation":
            toDelete = input("enter the station: ").title()
            if toDelete == "Stop":
                print("stop detected, stopping the current function")
                continue
            else:    
                if toDelete == s.search(toDelete):
                    print(s.search(toDelete),"is successfully deleted.")
                    s.deleteStation(toDelete)
                    lenUpd -= 1
#DET DISTANCE
        elif userInput.lower() == "getdistance":
            station1 = input("enter the first station: ").title()
            if station1 == "Stop":
                print("stop detected, stopping the current function")
                continue
            else:
                station2 = input("enter the second station: ").title()
                if station2 == "Stop":
                    print("stop detected, stopping current the function")
                    continue
                else:
                    print(f"The distace between {station1}and {station2} is :{s.distance(station1, station2)} station(s)")
            
#EXIT
        elif userInput.lower() == "exit":
            print("exit-> terminating the program.")
            break


if __name__ == "__main__":
    Start()
