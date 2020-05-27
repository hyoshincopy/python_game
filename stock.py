

def func():
    jabon = int(input('자본 입력: '))
    boochae = int(input('부채 입력: '))
    dang_gi_soon_eeik = int(input('당기 순이익 입력: '))
    stock_num = int(input('발행 주식 수 입력: '))
    present_price = int(input('현재 주가: '))
    # jasan = jabon+boochae
    roe = dang_gi_soon_eeik/jabon*100
    yogoosooikryul = 7.83
    chogoaeeik = jabon*(roe-yogoosooikryul)
    gi_up_gachi = jabon+(chogoaeeik/yogoosooikryul)
    price = gi_up_gachi/stock_num
    eps = dang_gi_soon_eeik/stock_num
    bps = jabon/stock_num
    per = present_price/eps
    pbr = present_price/bps
    # avg_5years_per = []
    # for i in range(0, 5):
    #     tmp = int(input('5년 동안의 PER 을 입력하세요 :'))
    #     avg_5years_per.append(tmp)
    print('========================')
    print('EPS ', eps)
    print('BPS ', bps)
    print('ROE ', roe)
    print('PBR', pbr)
    print('PER', per)
    print('적정가격 :', price)
    print('========================')
    print('(참고) PBR은 보통 1~2사이의 값이며 1보다 낮다면 저평가가 되고 있다는 뜻이다')
    print('(참고) PER은 주당 이익에 비해 주식가격이 낮다는것이므로 저평가가 되고있다는 뜻이다')
    # print('지난 5년간 per을 비교하여 만든 예상 적정주가 :(PER x EPS) ', avg_5years_per*eps)
    print('현재 가격: ', present_price)


func()
