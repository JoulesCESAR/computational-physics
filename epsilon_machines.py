# Script que calcula el epsilon de máquina

epsilon = 1
while 1 + 0.5*epsilon:
    epsilon = 0.5*epsilon
    print(epsilon)
    if epsilon == 0.0:
       break
