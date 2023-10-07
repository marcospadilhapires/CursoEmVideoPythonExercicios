import math
a = (float(input('Digite um angulo: ')))
r = math.radians(a)
print('O ângulo de {} tem o SENO de {:.2f}'.format(a, math.sin(r)))
print('O ângulo de {} tem o COSSENO DE {:.2f}'.format(a, math.cos(r)))
print('O ângulo de {} tem a TANGENTE DE {:.2f}'.format(a, math.tan(r)))
