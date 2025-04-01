from functools import cmp_to_key

def compare(item1,item2):
    if item1 < item2:
        return -1
    elif item1 > item2:
        return 1 
    else:
        return 0

class Item:
    def __init__(self,name):
        self.name = int(name)
    
#     def __lt__(self,other):
#         if self.name < other.name:
#             return -1
#         elif self.name > other.name:
#             return 1
#         else:
#             return 0
    # def __str__(self):
    #     return f"{self.name}"

class DynamicMeanFinder:
    def __init__(self):
        self.list = []

    def size(self):
        return len(self.list)
    
    def insert(self,item):
        self.list.append(item)
        self.list = sorted(self.list,key=cmp_to_key(compare))

    def find_median(self):
        median_idx = (self.size()-1) // 2
        median = self.list[median_idx]
        return median

    def remove_median(self):
        r = self.find_median()
        removed = self.list.remove(r)
        return r

    
def main():
    treasurer = DynamicMeanFinder()
    try:
        while True:
            inp = input()

            if not inp:
                break
            inp = inp.split(" ")
            
            if inp[0] == "I":
                treasurer.insert(int(inp[1]))

            elif treasurer.size() == 0 and (inp[0] == "M" or inp[0] == "R"):
                print(f"Invalid")
            else:
                if inp[0] == "M":
                    m =treasurer.find_median()
                    print(m)
                    
                if inp[0] == "R":
                    removed_median = treasurer.remove_median()
                    print(removed_median)
    except EOFError:
        pass
main()
