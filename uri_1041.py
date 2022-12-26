# Uri online Judge solving No- 1041  
x,y=list(map(float, input().split()))

if x==0 and y==0:
   print('Origem') 
elif x==0 or y==0:
   print("Eixo X") if y==0 else print("Eixo Y")
elif x>0:
   print('Q1') if y>0 else print('Q4')
else:
   print('Q2') if y>0 else print('Q3')

x,y,z = list(map(int, input().split()))

lst = [x,y,z]
lst.sort()
print(f'{lst[0]}\n{lst[1]}\n{lst[2]}\n')
print(f'{x}\n{y}\n{z}')