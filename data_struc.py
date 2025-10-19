class DataManagement:
    def __init__(self):
        self.item = []

    def add(self, value):
        add_new = self.item.append(value)
        return add_new

    def remove_beginning(self):
        #checks if the list has an element
        if len(self.item) == 0:
            print("List is empty")
        #removes the first element
        else:
            remove_item = self.item.pop(0)
            print(f"{remove_item} is removed")

    def remove_at_end(self):
        #checks if the list has an element
        if len(self.item) == 0:
            print("List is empty")
        #removes the first element
        else:
            remove_item = self.item.pop(-1)
            print(f"{remove_item} is removed")

    def remove_at(self, data):
        if not self.item:
            print("Item not found")
            return
        #removes a specific element from the list
        if data in self.item:
            self.item.remove(data)
            print(f"{data} is removed")
        else:
            print("Element is not found")

    def show_elements(self):
        print(f"Current List: {self.item}")
        

DM = DataManagement()

DM.add("Alpha")
DM.add("Beta")
DM.add("Charlie")
DM.add("Delta")
DM.show_elements()
DM.remove_at("Beta")
DM.remove_at_end()
DM.remove_beginning()
DM.show_elements()