'''
В институте биоинформатики по офису передвигается робот.
Недавно студенты из группы программистов написали для него программу, по которой робот, когда заходит в комнату,
считает количество программистов в ней и произносит его вслух: "n программистов".
Для того, чтобы это звучало правильно, для каждого nn нужно использовать верное окончание слова.
Напишите программу, считывающую с пользовательского ввода целое число nn (неотрицательное),
выводящее это число в консоль вместе с правильным образом изменённым словом "программист",
для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.
В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи,
как минимум до 1000 человек.
'''

n = int(input())
n1=n%10
n2=(n%10**2)//10
if n1==1 and n1!=n2:
  print(n,"программист")
elif (n1==2 or n1==4 or n1==3) and n2!=1:
  print(n,'программиста')
else:
  print(n,'программистов')