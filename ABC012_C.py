import io
import sys

_INPUT = """\
6
2013
2024
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  for i in range(1,10):
    if (45**2-N)%i==0 and 1<=(45**2-N)//i<10: print(i,'x',(45**2-N)//i)