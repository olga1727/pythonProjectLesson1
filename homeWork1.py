a = "Hi"
b = "everyone"
print(f"{a}, {b}")

num = [3, "three", {3}]
print(num)

num_a = int(input("Enter a number 0-9: "))
num_b = int(input("Enter another number 0-5: "))
print(num_a < num_b)

#

time = int(input("Enter any random number of seconds: "))
hours = time // 3600
minutes = time // 60 - hours * 60
seconds = time % 60
print(f"{hours:00}:{minutes:00}:{seconds:00}")

#

num = int(input("Enter any number greater than 0: "))
num = str(num)
print(f"{num} + {num + num} + {num + num + num} = {int(num) + int(num + num) + int (num + num + num)}")

#

num = int(input("Enter any number greater than 0: "))
greatest_dig = num % 10
num = num // 10

while num > 0:
    if num % 10 > greatest_dig:
        greatest_dig = num % 10
        if greatest_dig == 9:
            break
num = num // 10
print(f"Greatest digit in this number {num} is {greatest_dig}")

#

revenue = float(input("Enter your revenue (y.e.) "))
costs = float(input("Enter your float (y.e.) "))
result = revenue - costs
if result > 0:
    print(f"Your company  operates with profit {result} y.e.")
    print(f"The profitability of revenue is {100*(result/costs):.if}%")
    personal_n = int(input("How many employees work in your company?"))
    print(f"If you divide the profit between employees, then each employee will receive{result / personal_n:.3f} y.e.")
elif result < 0:
    print(f"Your company is operating at a loss {result} y.e.")
else:
    print(f"Your company has neither profit, nor loss. This is also a good result!")

#

while True:
    days = 1
    start_km = float(input("Your start result is: "))
    last_km = float(input("Your final result is: "))
    if start_km <= 0 or last_km < 0:
        print("Your results should be greater than 0. Your start result should be != 0.")
    else:
        while start_km < last_km:
            start_km += start_km * 0.1
            days += 1

            print(f"Sportsmen will achieve his result in {days} days")
            break

