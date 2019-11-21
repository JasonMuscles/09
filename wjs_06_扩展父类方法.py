
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

    def bark(self):

        # 1.针对子类特有的需求，编写代码
        print("神狗叫")
        # 2.使用super().调用原本在父类中封装的方法

        super().bark()
        # 父类名.方法(self)
        # Dog.bark(self)

        # 3.增加其他子类代码
        print("*****")


xtq = XiaoTianQuan()
# 重写了父类方法
xtq.bark()
