standard_input = '''2
4
1 1 4 1
3 4 2 1
7
5 4 5 4 5 4 5
3 2 4 7 2 5 9'''
for _ in range(int(input())):
    
    n = int(input())
    a = list(map(int, input().split()))
    d =  list(map(int, input().split()))
    best = -1
    survive = False
    for i in range(n):
        survive = (d[i] > (a[(i-1)%n] + a[(i+1)%n]))
        best = d[i] if (survive and d[i] > best) else best
    print(best)# cook your dish here
