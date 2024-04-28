import random
import time

player_victory = 0
enemy_victory = 0
for i in range(1, 4):
    player_life = random.randint(100, 150)
    player_attack = random.randint(30, 50)
    enemy_life = random.randint(100, 150)
    enemy_attack = random.randint(30, 50)

    print('【玩家】\n' + '血量：' + str(player_life) + '\n攻击：' + str(player_attack))
    print('------------------------')
    time.sleep(1)
    print('【敌人】\n' + '血量：' + str(enemy_life) + '\n攻击：' + str(enemy_attack))
    print('------------------------')
    time.sleep(1)

    while True:
        if enemy_life > player_attack and player_life > enemy_attack:
            enemy_life = enemy_life - player_attack
            print('你发起了攻击，【敌人】剩余血量' + str(enemy_life))
            player_life = player_life - enemy_attack
            print('敌人向你发起了攻击，【玩家】剩余血量' + str(player_life))
            print('------------------------')
            time.sleep(0.8)
        else:
            if enemy_life < player_attack and player_life > enemy_attack:
                print("本局结果：\n玩家胜利！")
                player_victory = player_victory + 1
                break
            elif enemy_life > player_attack and player_life < enemy_attack:
                print("本局结果：\n敌人胜利！")
                enemy_victory = enemy_victory + 1
                break
            elif enemy_life < player_attack and player_life < enemy_attack:
                print("本局结束\n双方平局")
                break
if player_victory > enemy_victory:
    print("玩家获得最终胜利！")
elif player_victory < enemy_victory:
    print("敌人获得最终胜利！")
elif player_victory == enemy_victory:
    print("双方平局")
