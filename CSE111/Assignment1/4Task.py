def solution(s1, s2):
    common_char = ""
    for char in s1:
        if char not in common_char:
            char_s1 = s1.count(char)
            char_s2 = s2.count(char)

            comm_num = [char_s1, char_s2]

            comm_i = min(comm_num)
            new_char = char * comm_i
            common_char += new_char

    return common_char


string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

result = solution(string1, string2)
print(result)
