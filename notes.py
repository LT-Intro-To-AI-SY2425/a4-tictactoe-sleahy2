# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog: 
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def __str__(self):
        return f"the dog's name is {self.name} and {self.name}'s age is {self.age}"

frankie = Dog("frankie" , 3)
logan = Dog("logan" , 8)
new_age = (int) (logan.age) * 1000
(str)(new_age)
print(logan)
