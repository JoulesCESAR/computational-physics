# Script que calcula el epsilon de máquina

epsilon = 1.0
while 1.0 + 0.5*epsilon != 1.0:
    epsilon = 0.5*epsilon
print(epsilon)
