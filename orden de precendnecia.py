n1=int (input('digite um valor '))
n2=int (input('digite outro valor'))
m= n1 * n2
s= n1 + n2
d= n1/ n2
di= n1// n2
e= n1** n2
print('A multiplicação é {} a soma {} a divisão {:.2f}'.format(m, s, d))
print(f"divisão inteira é {di}, já a potência é {e :.2f}")
print('A multiplicação é {} a soma {} a divisão {}'.format(m, s, d), end=' ')
print(f'divisão inteira é {di}, já a potência é {e}')