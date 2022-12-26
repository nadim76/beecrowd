# Uri Problem Solving No- 1046
a,b = map(int, input().split())

if a<b:
   print(f'O JOGO DUROU {b-a} HORA(S)')
else:
   print(f'O JOGO DUROU {(b+24)-a} HORA(S)')