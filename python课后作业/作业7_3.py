'''3、电影演员（入门）
补充一些代码，让其他人只要输入演员名，就打印出：××出演了电影××。'''

movies = {
    '妖猫传': ['黄轩', '染谷将太'],
    '无问西东': ['章子怡', '祖峰'],
    '超时空同居': ['雷佳音', '佟丽娅'],
}

actor = input('您想查询哪个演员？')
for movie in movies:
    actors = movies[movie]
    if actor in actors:
        print(actor + "出演了" + movie)
