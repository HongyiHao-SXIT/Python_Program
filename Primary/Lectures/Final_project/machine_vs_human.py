import random


class Player:
    def __init__(self):
        self.score = 0

    def make_move(self):
        while True:
            move = input("请输入你的选择（石头、剪刀、布）：")
            if move in ['石头', '剪刀', '布']:
                return move
            else:
                print("无效的输入，请重新输入。")


class Machine:
    def __init__(self):
        self.score = 0

    def make_move(self):
        choices = ['石头', '剪刀', '布']
        return random.choice(choices)


class Game:
    def __init__(self):
        self.player = Player()
        self.machine = Machine()
        self.rounds = 0

    def play_round(self):
        player_move = self.player.make_move()
        machine_move = self.machine.make_move()

        print(f"你出了：{player_move}")
        print(f"机器出了：{machine_move}")

        self.rounds += 1

        if player_move == machine_move:
            print("平局！")
        elif (player_move == '石头' and machine_move == '剪刀') or \
                (player_move == '剪刀' and machine_move == '布') or \
                (player_move == '布' and machine_move == '石头'):
            print("你赢了！")
            self.player.score += 1
        else:
            print("机器赢了！")
            self.machine.score += 1

    def play_game(self):
        while True:
            self.play_round()
            play_again = input("是否继续游戏？（是/否）：")
            if play_again.lower() != '是':
                break

        print(f"游戏结束，总共进行了{self.rounds}轮。")
        print(f"你的得分：{self.player.score}")
        print(f"机器的得分：{self.machine.score}")

        if self.player.score > self.machine.score:
            print("你赢得了游戏胜利！")
        elif self.player.score < self.machine.score:
            print("机器赢得了游戏胜利！")
        else:
            print("游戏平局！")


if __name__ == "__main__":
    game = Game()
    game.play_game()