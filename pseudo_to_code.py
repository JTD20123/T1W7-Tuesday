# -Example 1: Calcualating the sum of a list of numbers
# ---
#     Initialise sum to 0
#     For each number in the list
#         ADD the number to sum
#     END FOR 
#     Print sum

numbers = [1,2,3,4,5]

total_sum = 0

for number in numbers:
    total_sum += number

print(total_sum)