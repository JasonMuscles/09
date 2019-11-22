class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("普通狗玩耍~")


class XiaoTianQuan(Dog):

    def game(self):
        print("神狗玩耍~~~")


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 愉快玩耍" % (self.name, dog.name))

        # 让狗玩耍
        dog.game()


# 1.创建一个狗对象
# wangcai = Dog("wangcai")
wangcai = XiaoTianQuan("哮天犬")
# 2.创建一个小明对象
xiaoming = Person("小明")

# 3.让小明调用和狗玩耍的方法
xiaoming.game_with_dog(wangcai)
