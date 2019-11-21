class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):

    def bark(self):
        print("狗叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("可以飞翔")


# 创建一个哮天犬的对象
xtq = XiaoTianQuan()
xtq.fly()
