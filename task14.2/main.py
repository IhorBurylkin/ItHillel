from classes import Student, Group, GroupIsFullError

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

try:
    for i in range(1, 11): 
        st = Student('Male', 20+i, f'Name{i}', f'Lastname{i}', f'AN{i}')
        gr.add_student(st)
except GroupIsFullError as e:
    print(f'The group is full: {e}')

print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

assert gr.find_student('Jobs') == st1

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!