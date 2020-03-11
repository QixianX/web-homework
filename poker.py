def judge(black_list, white_list):
    # 数值颜色分离
    black_number = []
    black_color = []
    white_number = []
    white_color = []
    for i in black_list:
        a = list(map(i))
        black_number.append(a[0])
        black_color.append(a[1])
    for j in white_list:
        b = list(map(j))
        white_number.append(b[0])
        white_color.append(b[1])

    # 替换数字字符为数字10,11....
    rep = {'T':'10','J':'11','Q':'12','K':'13','A':'14'}
    temp1 = [rep[i] if i in rep else i for i in black_number]
    temp2 = [rep[i] if j in rep else j for j in white_number]
    black_number = [int(i) for i in temp1]
    white_number = [int(j) for j in temp2]

    # 条件判断
    black_number = black_number.sort()
    white_number = white_number.sort()
    blnu_com = {}
    whnu_com = {}
    blco_com = {}
    whco_com = {}

    # 统计相同数值情况
    for i in black_number:
        if black_number.count(i) >= 1:
            blnu_com[i] = black_number.count(i)
    for i in white_number:
        if white_number.count(i) >= 1:
            whnu_com[i] = white_number.count(i)

    # 顺子
    if (black_number[4] - black_number[0]) == 4:
        bsz_flag = 1
    if (white_number[4] - white_number[0]) == 4:
        wsz_flag = 1

    # 同花
    for i in black_color:
        if black_color.count(j) == 5:
            bth_flag = 1
    for j in white_color:
        if white_color.count(j) == 5:
            wth_flag = 1

    # 对子 两对
    wd , bd = 0
    bs , ws = 0 
    bt , wt = 0 
    for i in blnu_com:
        if i == 2:
            bd += 1
        if i == 3:
            bs += 1
        if i == 4:
            bt += 1
    for j in whnu_com:
        if j == 2:
            wd += 1
        if j == 3:
            ws += 1
        if j == 4:
            wt = 1 
            
    if bd == 1 and bs != 1:
        bdz_flag = 1
        
    if wd == 1 and ws != 1:
        wdz_flag = 1

    # 两对
    if bd == 2:
        bld_flag = 1
    if wd == 2:
        wld_flag = 1
 
    # 三条  葫芦  三条+对子。 比较三张大小一样的牌的牌点数。
    if bs == 1:
        bhl_flag =1

    if ws == 1:
        whl_flag = 1

    # 铁支  有四张同样大小的牌片。 比较四张大小一样的牌的牌点数。
    if bt == 1:
        btz_flag = 1
    if wt == 1:
        wtz_flag = 1



    



    










    pass











if __name__ == '__main__':

    black_list = []
    white_list = []
    for i in range(0,4):
        print("输入black方手牌")
        black_list.append(input())
    for j in range(0,4):
        print("输入white方手牌")
        white_list.append(input())

    print(judge(black_list, white_list))
    