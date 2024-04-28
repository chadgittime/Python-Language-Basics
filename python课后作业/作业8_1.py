# globaltimes、再PK（中等）
# 要求：在今天项目代码practice8_1.py的基础上，添加一个新功能：每盘（3局）游戏结束后，游戏会问我们是否要继续游戏，再加一盘。我们可以选择再来一盘，也可以选择退出游戏。
import random
import time

player_victory = 0
enemy_victory = 0

while True:
    for i in range(1, 4):
        time.sleep(0.3)
        print('  \n——————现在是第 %s 局——————' % i)
        player_life = random.randint(100, 150)
        player_attack = random.randint(30, 50)
        enemy_life = random.randint(100, 150)
        enemy_attack = random.randint(30, 50)

        print('【玩家】\n血量：%s\n攻击：%s' % (player_life, player_attack))
        print('------------------------')
        time.sleep(1)
        print('【敌人】\n血量：%s\n攻击：%s' % (enemy_life, enemy_attack))
        print('-----------------------')
        time.sleep(0.3)

        while player_life > 0 and enemy_life > 0:
            player_life = player_life - enemy_attack
            enemy_life = enemy_life - player_attack
            print('你发起了攻击，【敌人】剩余血量%s' % enemy_life)
            print('敌人向你发起了攻击，【玩家】的血量剩余%s' % player_life)
            print('-----------------------')
            time.sleep(0.3)

        if player_life > 0 and enemy_life <= 0:
            player_victory += 1
            print('敌人死翘翘了，你赢了！')
        elif player_life <= 0 and enemy_life > 0:
            enemy_victory += 1
            print('悲催，敌人把你干掉了！')
        else:
            print('哎呀，你和敌人同归于尽了！')

    if player_victory > enemy_victory:
        time.sleep(0.3)
        print('\n【最终结果：你赢了！】')

    elif enemy_victory > player_victory:
        print('\n【最终结果：你输了！】')

    else:
        print('\n【最终结果：平局！】')

    while True:
        choice = input("是否要继续游戏？\n请回答再来一局或退出游戏\n")
        if choice == '再来一局':
            break
        elif choice == '退出游戏':
            exit()
        else:
            continue
