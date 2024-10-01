# start
import random

list_95_105: list[int] = [i for i in range(95, 106)]
print(list_95_105)

list_even: list[int] = [i for i in range(10, 21, 2)]
print(list_even)

list_bool: list[bool] = [random.choice([True, False]) for _ in range(5)]
print(list_bool)

list_1_100: list[int] = [random.randint(1, 101) for _ in range(10)]
print(list_1_100)

list_50: list[int] = [i for i in list_1_100 if i > 50]
print(list_50)

# bonus
# list_connected: list[int] = [random.randint(1 , 101) for i in range(10) if i > 50] # doesnt working
# print(list_connected)

# bonus
# list_input : list[str] = [ for letter in input("Enter a sentence:") ]

list10_99: list[int] = [random.randint(10, 100) for _ in range(10)]
print(list10_99)

list_ahadot: list[int] = [number % 10 for number in list10_99]
print(list_ahadot)
