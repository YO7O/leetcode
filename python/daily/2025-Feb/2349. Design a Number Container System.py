from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.num_indices = defaultdict(SortedList)
        self.index_num = {}
        
    def change(self, index: int, number: int) -> None:
        if index in self.index_num:
            old = self.index_num[index]
            self.num_indices[old].discard(index)
            if not self.num_indices[old]:
                del self.num_indices[old]
        self.num_indices[number].add(index)
        self.index_num[index] = number

    def find(self, number: int) -> int:
        if number in self.num_indices:
            return self.num_indices[number][0]
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)