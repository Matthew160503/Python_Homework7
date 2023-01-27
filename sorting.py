def name_sorting():
    with open("spravocnik.txt","r+") as text:
        out = text.readlines()
        list = []
        for line in out:
            temp = line.split()
            list.append(temp)
        list = sorted(list, key = lambda x: x[1])
        text.seek(0)
        for data in list:
            text.write(' '.join(data))
            text.write('\n')
        print('Сортировка окончена')

def id_sorting():
    with open("spravocnik.txt","r+") as text:
        out = text.readlines()
        list = []
        for line in out:
            temp = line.split()
            list.append(temp)
        list = sorted(list, key = lambda x: x[0])
        text.seek(0)
        for data in list:
            text.write(' '.join(data))
            text.write('\n')
        print('Сортировка окончена')