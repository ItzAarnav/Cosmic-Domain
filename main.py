
integer = 1
float = 0.1
boolean = True
list = [1, 2, 3, "string"]
strings = "12, text"
dictionary = {
    "key":"value",
    "aarnav":"cool",
}
tuple = (1, 2, "2")
sets = {1, 2, 3}

with open("numbers.txt", 'r') as file:
    numbers = file.read().split()

multiply = lambda x, y: x * y
print(multiply(1, 2))

a = 10
b = a
