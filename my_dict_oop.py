
class ListManager:
    def __init__(self):
        self.list1 = []
        self.list2 = []
        self.dictionary = {}


    def get_list_input(self, list_name):
        print(f"Entering values for {list_name}:")
        while True:
            value = input("Enter value: ")
            self.list1.append(value) if list_name == "List 1" else self.list2.append(value)
            response = input("Are you through? (yes/no): ")
            if response.lower() == "yes":
                break

    def check_list_lengths(self):
        if len(self.list1) != len(self.list2):
            print("Length of lists don't match")
            return False
        else:
            print("Lengths match. Proceeding")
            for _ in range(3):
                print(".")
                time.sleep(1)
            return True

    def create_dictionary(self):
        for i in range(len(self.list1)):
            self.dictionary[self.list1[i]] = self.list2[i]
        return self.dictionary

def main():
    manager = ListManager()
    manager.get_list_input("List 1")
    manager.get_list_input("List 2")
    if manager.check_list_lengths():
        dictionary = manager.create_dictionary()
        print("Dictionary:", dictionary)

if __name__ == "__main__":
    main()









