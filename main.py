# Add leading zeros to a number in Python

num = 246


result_1 = str(num).zfill(5)
print(result_1)  # 👉️ '00246'

result_2 = str(num).zfill(6)
print(result_2)  # 👉️ '000246'