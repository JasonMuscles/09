
class Tool(object):

    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name

        Tool.count += 1


# 创建工具对象
tools = Tool("斧头")
tools1 = Tool("扳手")
tools2 = Tool("剪刀")

# 调用类方法
Tool.show_tool_count()

