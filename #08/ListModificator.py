
class ListModificator:
    def __init__(self):
        self.my_num_list = []
    
    def first(self):
        return self.my_num_list[0]
 
    def last(self):
        return self.my_num_list[len(self.my_num_list)-1]
 
    def add(self, num):
        self.my_num_list.append(num)

    def pop_first(self):
        return self.my_num_list.pop(0)
 
    def pop_last(self):
        return self.my_num_list.pop()

    def leght(self):
        return len(self.my_num_list)
    
instance_list_modificator = ListModificator()
for i in range(1,11):
 instance_list_modificator.add(i)
print(instance_list_modificator.my_num_list)
instance_list_modificator.pop_last()
print(instance_list_modificator.my_num_list)
instance_list_modificator.pop_first()
print(instance_list_modificator.my_num_list)
print(instance_list_modificator.leght())