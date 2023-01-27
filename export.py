def output_all_information():
    with open("spravocnik.txt","r") as text:
        for out in text.readlines():
            print(out, end="")
    print('\nВся информация выведена!')

def output_names():
    with open("spravocnik.txt","r") as text:
        for line in text.readlines():
            line = line.split()
            print(f'Имя - {line[1]}, Фамилия - {line[2]}') 