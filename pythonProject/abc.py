def sayhi(name, age):
    print("hello " + name + ", you are" + age)

sayhi("Sahithya", " 18")

def cube(num):
   return num*num*num

result = cube(5)
print(result)

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are tall but not a male")

else:
    print("You are not a male")

