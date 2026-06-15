a_list = [3,4,2,5,7,1,6,8,9]
b_list = []



while len(a_list) != 0:
    first_element = a_list[0]
    for element in a_list:
        if first_element < element:
            first_element = element
    a_list.remove(first_element)
    b_list.append(first_element)
print(b_list)
print(a_list)
