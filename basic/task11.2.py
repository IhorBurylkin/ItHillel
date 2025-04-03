from inspect import isgenerator

def generate_cube_numbers(end):
    num = 2
    while True:
        cube_num = num ** 3
        if cube_num < end + 1:
            yield cube_num
            num += 1
        else:
            break

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True
assert list(generate_cube_numbers(10)) == [8]
assert list(generate_cube_numbers(100)) == [8, 27, 64]
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000]
print('Ok')