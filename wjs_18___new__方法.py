class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):

        # 1.创建对象时,new方法会被自动调用
        print("new方法")

        # 2.为对象分配空间
        instance = super().__new__(cls)

        # 3.返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化")


# 创建播放器对象
player = MusicPlayer()
player1 = MusicPlayer()
player2 = MusicPlayer()

# 多个对象输出地址空间都不相同
print(player)
print(player1)
print(player2)

