prices = [2,5,1,3,4]
result = 0

stop_state = 0


profit_list = [[0]*1 for _ in range(len(prices))]
for i in range(len(prices)) :
    for j in range(1,len(prices)) :
        cur_profit = prices[j] - prices[i]
        profit_list[j].append(cur_profit)
    

print(profit_list)