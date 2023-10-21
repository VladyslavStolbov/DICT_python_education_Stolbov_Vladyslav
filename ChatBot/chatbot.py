print("Hello! My name is Alex\nI was created in 2023")
name = input("Please, remind me your name.\n")
print("What a great name you have, " + name + "!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print("Your age is " + str(age) + "; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
number = int(input())
count = 0
for n in range(number + 1):
    if count <= number:
        print(str(count) + " !")
        count += 1
print("Completed, have a nice day!")
print("Let's test your programming knowledge.")
print("What is an 'IDE' in programming?")
print("1. Integrated Development Environment\n2. Internet Data Exchange\n3. Instructional Design Environment\n4. "
      "Intelligent Debugging Engine")
answer = int(input())
while answer != 1:
    print("Please, try again.")
    answer = int(input())
print("Completed, have a nice day!")
print("Congratulations, have a nice day!")