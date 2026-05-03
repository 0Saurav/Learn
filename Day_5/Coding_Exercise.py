# Highest score

student_scores = [150, 122, 155, 149, 68, 42, 56, 89, 171, 153, 70, 65, 91]


# Use of sum() function
total_score = sum(student_scores)
print(total_score)


sum = 0
for score in student_scores:
    sum += score

print(f"Total score is: {sum}")

# finding maximum value: 

max_value = 0
for score in student_scores:
    if score > max_value:
        max_value = score
    else:
        max_value = max_value

print(f"Maximum value is {max_value}")

# Using max() function

max_value = max(student_scores)
print(max_value)