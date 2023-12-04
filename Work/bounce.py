# bounce.py
#
# Exercise 1.5

height = 100 # 100 meters
return_height = 0.6 # 3 / 5 or 0.6 bounce back
bounces = 10 # 10 bounces

while bounces >= 1:
    height *= 0.6
    print(bounces, round(height, 4))
    bounces -= 1

pass

