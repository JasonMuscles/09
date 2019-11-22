class Tool(object):

    # 使用赋值语句定义类属性,记录共计对象的数量
    count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性的值+1
        Tool.count += 1


# 1.创建工具对象
tools = Tool("斧头")
tools1 = Tool("钳子")
tools2 = Tool("扳手")

# 2.输出工具对象的总数
tools.count = 88

print("工具对象数量 %d" % tools.count)
print("真实工具对象数量 %d" % Tool.count)