
from rich import print

# List

list_1 = []
list_2 = list()

# Dict

dict_1 = {
    'name': 'Damien',
}
dict_2 = dict(
    name='Damien'
)

# Class

class Demo():
    def __init__(self, dict_2):

        # manual attribution to self.data
        # self.data = dict_2
        # print(self.data) # {'name': 'Damien'}


        # use class.function() set_data to set dict_2 to self.data
        self.set_data(dict_2)


    def set_data(self, new_dict:dict) -> dict:
        self.data = new_dict
        name = self.data.get('name')
        if name != None:
            self.set_name(name)
        return self.data

    def get_data(self) -> dict:
        return self.data

    def set_name(self, new_name:str) -> str:
        self.name = new_name
        return self.name

    def get_name(self) -> str:
        return self.name


class_demo = Demo(dict_2)

print('class_demo' ,class_demo) # <__main__.Demo object at 0x7f1b987acfd0>
print('----------')

list_1.append(class_demo)

# on accede directement a la valeur self.data depuis .__dict__['data']
class_demo_dict_data = class_demo.__dict__['data']

print('class_demo_dict_data' ,class_demo_dict_data) # {'name': 'Damien'}
print('----------')

list_1.append(class_demo_dict_data)
class_demo_dict = class_demo.__dict__

print('class_demo_dict' ,class_demo_dict)
print('----------')

list_1.append(class_demo_dict)

print('class_demo.set_data()' ,class_demo.set_data({'name': 'python'}))
print('----------')

list_1.append(class_demo_dict)
