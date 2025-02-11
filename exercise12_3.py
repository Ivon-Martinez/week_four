#we have to import the random library
import random
#we need to store 6 uniques numbers, and for that reason we use set as it will not have repeated numbers
lotto_numbers = set()
# we have to add 6 numbers to our lotto variable, so we use the while loop to make sure that
# once lotto_numbers has 6 elements then it will get out of the loop
while len(lotto_numbers) < 6:
#we want them to be random numbers, so that's why we use random.randint,
# which takes two arguments to define the range as we want it to go from 1 to 50, both numbers are inclusive
    lotto_numbers.add(random.randint(1, 50))
print(f"Your lotto ticket is: ", *lotto_numbers, f"\nGood luck {chr(128578)}")

#randon module, .sample() method