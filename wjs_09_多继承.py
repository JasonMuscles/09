class A:
    def test(self):
        print("A——test方法")


class B:
    def demo(self):
        print("B-—demo方法")


class C(A, B):
    """多继承-可以让子类同事有多个父类的属性和方法"""
    pass


# 创建一个子类对象c
c = C()

c.test()
c.demo()