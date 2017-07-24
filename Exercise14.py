def remove_duplicates(input_list):
    output_list = []
    counter = 0
    for i in input_list:
        for j in output_list:
            if i == j:
                counter += 1
        if counter == 0:
            output_list.append(i)
        counter = 0
    return output_list


def remove_duplicates_set(input_list):
    output_set = set()
    for i in input_list:
        output_set.add(i)
    return output_set

sample_list = [1, 1, 2, 4, 5, 12, 2, 24, 5, 12, 12, 1]

print(remove_duplicates(sample_list))
print(remove_duplicates_set(sample_list))