from calulate import distributionSequence

q = 1
while (q):
	n = int(input("输入n:"))
	k = int(input("输入k:"))
	p = float(input("输入p:"))
	if (n > 1 and k > -1 and (p < 1 and p > 0)):#n>2;0<=k<=n;0<p<=1#p=1,ans = 0;
		distributionSequence(n, k, p)
	q = int(input("是否继续(是/否;1/0):"))
