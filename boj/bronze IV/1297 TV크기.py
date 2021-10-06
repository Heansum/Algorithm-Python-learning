D, H, W = input().split(' ')

D = int(D)
H = int(H)
W = int(W)

double_d = D * D
double_h = H * H
double_w = W * W

a = (double_d / (double_h + double_w))
a = a**(1/2)

H = a * H
H = int(H)
W = a * W
W = int(W)

print(H, W, sep=" ")