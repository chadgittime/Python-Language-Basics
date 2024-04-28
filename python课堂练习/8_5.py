import random
import time

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
        break
