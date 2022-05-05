import io
import sys

_INPUT = """\
6
3661
86399
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  print(str(N//3600).zfill(2),':',str(N%3600//60).zfill(2),':',str(N%3600%60).zfill(2),sep='')