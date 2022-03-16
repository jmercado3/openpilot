#!/Users/haiiro/.pyenv/shims/python3
from math import exp

def a(l,al,t):
  return al * exp(-l * t * t / 2)

al=-1
vl=-20
xl=100
l=1.5
t0=0
for l in [1.0, 1.5, 2.0]:
  al=-1
  vl=-20
  xl=100
  t0=0
  print(f"{l = :3.3f}")
  for i in range(10):
    dt = 0.2 if i <= 4 else 0.6
    al = a(l,al,t0)
    xl += vl * dt
    vl += al * dt
    print(f"{t0 = :3.3f}, {al = :3.3f}, {vl = :3.3f}, {xl = :3.3f}")
    t0+=dt