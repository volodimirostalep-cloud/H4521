class student:
    def __init__(self, name, height=100):
        self.height = height
        self.name = name
        #print("Hello, i am {self.name}")

    def print(self):
         print(f"{self.name}:")
         print("------------------------------------------")
         print(f"Скількі в мене градусів {self.height}")

    def grow(self4):
        self4.height -= 75

    def grow(self1):
        self1.height -= 80

    def grow(self2):
        self2.height -= 70

st4 = student("Pivko")
st4.grow()
print(st4. height)
print(st4.name)

st1 = student("Vodochka", 200)
st1.grow()
st1.grow()
print(st1. height)
print(st1.name)

st2 = student("Viscarick", 190)
st2.grow()
st2.grow()
print(st2. height)
print(st2.name)
