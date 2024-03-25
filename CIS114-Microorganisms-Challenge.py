def Calculate_pop():
    start_num = int(input("Enter the starting number of organisms: "))
    avg_daily_inc = int(input("Enter the average daily increase by percentage: "))
    num_of_days = int(input("Enter the number of days to multiply: "))

    my_data = {}

    for i in range(num_of_days):
        day_num = i+1
        my_data[day_num] = start_num
        start_num = (start_num * (100+avg_daily_inc))/100

    print("{:<20} {:<10}".format('Day Approximate', 'Population'))
    print("{:<30}".format('--------------------------------'))
    for k, v in my_data.items():

        print("{:<20} {:<10}".format(k, v))

Calculate_pop()



