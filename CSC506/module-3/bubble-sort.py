number = [3,48,97,34,15,68,97,15,63,48,4,1,15,69]

def bubble_sort(list):
    for x in range(len(list)):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
        print(list)
    print(list)

bubble_sort(number)