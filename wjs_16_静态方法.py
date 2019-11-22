class Dog(object):

    @staticmethod
    def run():

        # 不访问实例属性/类属性
        print("小狗子跑。。。。。。")


# 调用静态方法 -- 不需要创建对象也可直接调用
print(Dog.run())
