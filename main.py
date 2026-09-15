import random
class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 55
        self.enegry = 200
        self.alive = True

    def study(self):
        print("I went to hight school")
        self.enegry -= 5
        self.progress += 2.5
        self.gladness -= 2

    def chill(self):
        print("I went outside with friends")
        self.gladness += 3
        self.enegry -= 5
        self.progress -= 0.5


    def sleep(self):
        print("I went asleep")
        self.enegry += 5
        self.gladness += 1

    def eat(self):
        print("It was deliicious")
        self.enegry += 2.5
        self.gladness += 1
        self.progress -= 0.5

    def is_alive(self):
        if self.progress <= 0:
            print("My mind is so mud")
            self.alive = False
        if self.gladness <= 0:
            print("Noone cars about me")
            self.alive = False
        if self.progress > 100:
            print("I becem a master")
        if self.enegry <= 0:
            print("pls kill me someone")
            self.alive = False


    def live(self, day):
        print(f"Day №{day} from live {self.name}")
        print("-"*30)
        rnd = random.randint(1,4)
        if rnd == 1:
            self.study()
        elif rnd == 2:
            self.chill()
        elif rnd == 3:
            self.sleep()
        else:
            self.eat()

        self.info()
        self.is_alive()
        print()

    def info(self):
        print(f"For to day {self.name} has:")
        print(f"Happy : {self.gladness}")
        print(f"IQ {self.progress}")
        print(f"Enegry {self.enegry}")


student = Student("Vodochka")
day = 1
while student.alive == True:
      student.live(day)
      day += 1
