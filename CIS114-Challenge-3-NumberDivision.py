def divisorsOfNumber(user_input):
    divisor = 1
    my_divisors = []
    while user_input >= divisor:
        if user_input % divisor == 0:
            my_divisors.append(divisor)
        divisor += 1

    return my_divisors


def perfectNumbers(integer):
    my_divisor_list = divisorsOfNumber(integer)
    biggest_num = my_divisor_list[-1]
    a = 1
    sum = 0
    perfect_num_list = []
    while a <= (biggest_num):
        my_list = divisorsOfNumber(a)
        my_list.pop()
        for i in my_list:
            sum +=i

        if sum == a:
            perfect_num_list.append(sum)
            sum=0

        else:
            sum=0


        a += 1

    print(perfect_num_list)

perfectNumbers(10000)