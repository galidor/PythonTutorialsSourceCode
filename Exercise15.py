def reverse_order(input_string):
    words = input_string.split()
    words = words[::-1]
    output_string = ""
    for i in words:
        output_string = " ".join(words)
    return output_string


sample_string = "I like bread but I prefer bananas to it"
print(reverse_order(sample_string))