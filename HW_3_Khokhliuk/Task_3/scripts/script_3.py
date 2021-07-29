list_1 = [1, 2, "3.0", "f", 4, "4", "sd", '14', '4f']
list_2 = []


def nums(count_nums):
    def wrap():
        for i in list_1:
            if type(i) == int:
                list_2.append(i)
            elif type(i) == float:
                list_2.append(i)
            elif type(i) == str:
                try:
                    int(i)
                    list_2.append(int(i))
                except ValueError:
                    try:
                        float(i)
                        list_2.append(float(i))
                    except ValueError:
                        pass
            else:
                pass
        print(list_2)
        result = count_nums(list_2)
        return print(result)
    return wrap


@nums
def count_nums(x):
    print(sum(x))


count_nums()
