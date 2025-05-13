import random
start = int(input())
end = int(input())
answer = int(input())
random_number = random.randint(start, end)
if answer > random_number:
    print("the guess is too big!...")
if answer < random_number:
    print(" the guess is too short!...")
if answer == random_number:
    print("wow! you got the answer...")

