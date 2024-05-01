t = int(input())
for _ in range(t):
    n = int(input())
    mat_sum = 0
    out_seq = ''
    for i in range(n):
        mat_sum += (i+1)*(2*(i+1)-1)
        out_seq += str(i+1)+' '
    print(str(mat_sum)+' '+str(2*n))
    for i in range(n):
        print("1 "+str(n-i)+' '+out_seq)
        print("2 "+str(n-i)+' '+out_seq)