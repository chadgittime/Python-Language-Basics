import random
import time

player_victory = 0
enemy_victory = 0

while True:
    for i in range(1, 4):
        time.sleep(0.3)
        print('  \n——————现在是第 {} 局——————'.format(i))
        player_life = random.randint(100, 150)
        player_attack = random.randint(30, 50)
        enemy_life = random.randint(100, 150)
        enemy_attack = random.randint(30, 50)

        print('【玩家】\n血量：{}\n攻击：{}'.format(player_life, player_attack))
        print('------------------------')
        time.sleep(0.3)
        print('【敌人】\n血量：{}\n攻击：{}'.format(enemy_life, enemy_attack))
        print('-----------------------')
        time.sleep(0.3)

        while player_life > 0 and enemy_life > 0:
            player_life = player_life - enemy_attack
            enemy_life = enemy_life - player_attack
            print('敌人发起了攻击，【玩家】剩余血量{}'.format(player_life))
            print('你发起了攻击，【敌人】的血量剩余{}'.format(enemy_life))
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

    a1 = input('要继续游戏吗，请输入n退出，输入其他继续：')
    if a1 == 'n':
        break
