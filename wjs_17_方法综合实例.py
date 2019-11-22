class Game(object):

    # 类属性 - 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("游戏说明文档~~")

    @classmethod
    def show_top_score(cls):
        print("最高得分为 %.2f" % cls.top_score)

    def star_game(self):
        print("%s 准备开始游戏" % self.player_name)


# 1.查看游戏的帮助信息
Game.show_help()

# 2.查看历史最高分
Game.show_top_score()

# 3.创建游戏对象
games = Game("Jason")
Game.top_score = 99
games.star_game()

Game.show_top_score()
