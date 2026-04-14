# Finds average of a list of scores

from cs50 import get_int

scores = [72, 73, 33] 

average = sum(scores) / len(scores)
print(f"Average: {average}")

scores = [] # Empty list possible in Python not C

# Append method and concatenation
for i in range(3):
    score = get_int("Score: ")
    #scores.append(score)
    scores = scores + [score]   # Concatenate to list

average = sum(scores) / len(scores)
print(f"Average: {average}")