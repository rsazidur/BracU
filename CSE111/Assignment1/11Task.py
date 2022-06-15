def input_frequency(number):

    global ref_list
    temp = [int(number)]
    ref_list += temp
    frequency = dict((num, ref_list.count(num)) for num in ref_list)
    return frequency


user_input = input()
ref_list = []
while user_input != "STOP":
    result = input_frequency(user_input)
    user_input = input()

input_prompt = result.keys()
input_prompt = sorted(input_prompt)

for value in input_prompt:
    print(f"{value} - {result[value]} times")