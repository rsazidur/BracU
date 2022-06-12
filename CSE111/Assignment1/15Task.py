def div_sum(min, max, div):
    if div != 0:

        sum1 = 0
        for num in range(min, max):
           if num % div == 0:
               sum1 += num
        return sum1

    else:
        return "Divisor cannot be 0."


minimum = int(input("Minimum: "))
maximum = int(input("Maximum: "))
divisor = int(input("Divisor: "))
print(div_sum(minimum, maximum, divisor))

