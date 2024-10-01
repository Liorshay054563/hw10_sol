# start


## a -- try - except give us a safety net, if user put wrong input the code will not collapse
## b -- we have to 'cache' the error before ist happening to guide the user input correctly

## c
try:
    x: float = 88 / 0
    print(x)
except:
    print("done")

## d
try:
    y: int = int(input("Enter positive number:"))
    if 0 > y:
        raise ValueError(f"{y} is not positive")  # this code not working

except:
    print("ok")

## e
list_index4: list[int] = []
for i in range(5):
    list_index4.append(0)

SENTINEL = -999

while True:
    try:
        x: int = int(input(" Enter a number:"))
        if x == SENTINEL:
            break
        if not 0 <= x <= 4:
            continue
        list_index4[x] += 1
        # i try to put the "except" here but the code didn't run good

        print("statistics :", end=" ")
        for i in range(5):
            if list_index4[i]:
                print(f"[{i}]: {list_index4[i]}", end=" ")
    except ValueError as e:
        print("You Don't enter a number")
        print(e)
