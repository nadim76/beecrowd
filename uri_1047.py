a,b,c,d = map(int, input().split())

start = (a*60)+b
end = (c*60)+d

dif = end - start
if dif<=0:
   dif = dif+24*60

hours = dif // 60
minutes =dif % 60

print(f'O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)')