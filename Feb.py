def Feb(n):
    '''
    返回第N个斐波那契数
    :param n:
    :return:
    '''
    # 1 1 2 3 5 8 13 21
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a

if __name__=="__main__":
    for i in range(1,9):
        print(Feb(i))