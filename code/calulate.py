N = 1000  # 排列组合计算后的值的最大长度(位),用于初始化数组

def distributionSequence(n, k, p):
	head = 1    #二项分布列的头部C(n,k),默认k = 0或k = n,head = 1，否则head = 0

	#排列组合计算，计算头部：head = C(n,k)
	if(0 < k < n):
		head = 0
		#取k,和n-k，分辨大小
		min_mun = min(k, (n - k))
		max_mun = max(k, (n - k))

		# 初始化排列组合计算后的值存放的数组，最大为N位
		Data = [0 for i in range(1, N + 1)]
		Data[0] = 1 #第0位不取
		Data[1] = 1 #低位置为1
		digit = 1   #位数

		#公式化简，分母部分为n * (n-1) * (n-2) * ... * max_mun-1；分母为min_mun * (min_mun-1) * ... * 1
		#把需要进行相乘的数放入分母数组、分子数组
		# 初始化分母数组和分子数组；数组的第0位置不使用
		data_max = [i for i in range(n + 1, max_mun, -1)]   #分母，从大到小
		data_min = [i for i in range(min_mun + 1, 0, -1)]   #分子，从大到小
		data_max[0] = 0 #0位不取
		data_min[0] = 0 #0位不取

		# 存放奇数的公约数，范围2~min_mun，用作分母和分子约分，范围约束：分子最大为min_mun
		base = [i for i in range(1, min_mun + 1, 2)]
		# 1约分无意义，把1变成2
		base[0] = 2

		# 用数组模拟人工约分;分子和分母从最值大开始约分
		for j in range(1, min_mun + 1):
			for i in range(1, min_mun + 1):
				if ((data_max[i] % data_min[j] == 0) and (data_min[j] != 1) and (data_max[i] != 1)):#分母是分子的倍数，分子可以被分母全部约分；分母为1为约尽，分子为1为约尽
					data_max[i] = data_max[i] // data_min[j]    #分母取商
					data_min[j] = 1 #分子被全部约掉，置为1
				else:
					for t in range(0, len(base)): #公约数的长度次循环
						if (data_max[i] % base[t] == 0) and (data_min[j] % base[t] == 0): #分母和分子存在公约数
							data_max[i] = data_max[i] // base[t]    #分母用公约数约分
							data_min[j] = data_min[j] // base[t]    #分子用公约数约分
							break

		# 用数组模拟人工乘积，最后一个数组值堆积(最大1.7976931348623157e+308)；
		for i in range(1, min_mun + 1):#循环次数为分母数组的长度
			for j in range(1, digit + 1):
				Data[j] = Data[j] * data_max[i]#分母每位数组的阶乘（约分后的分母）
			for j in range(1, digit + 1):#每乘一次处理每位数组的长度，从低位开始
				if (Data[j] >= 10):
					for r in range(1, digit + 1):
						if (Data[digit] > 9):#当最高位大于9则位数加1
							digit = digit + 1
						Data[r + 1] = Data[r + 1] + Data[r] // 10#进位的位重置
						Data[r] = Data[r] % 10#进位后的位重置

		# 处理最后一个数组
		str_end_digit = str(Data[digit])  # Data[digit]的值变为字符串
		list_end_digit = list(map(int, str_end_digit[::-1]))  # 字符串反转，拆分并保存到list_end_digit数组
		# 数组衔接；把Data[digit]拆分后接回Data数组
		for i in range(0, len(str_end_digit)):
			Data[digit + i] = list_end_digit[i]
		digit = digit + len(str_end_digit)-1#总共的位数

		#把数组里面的数据转换成一个整数，最大值不超过308位
		for i in range(1, digit + 1):
			head = head + Data[i] * 10 ** (i - 1)


	#计算尾部：tail = p^k*(1-p)^(n-k)
	tail = pow(p,k) * pow((1-p),(n-k))
	#分布列计算的结果，头部*尾部
	ans = head*tail
	print(ans)
	print()
	return 0
