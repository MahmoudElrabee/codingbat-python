def no_teen_sum(a, b, c):
  sum = 0
  if(not(a>=13 and a<=19) or a==15 or a == 16): sum += a
  if(not(b>=13 and b<=19) or b==15 or b == 16): sum += b
  if(not(c>=13 and c<=19) or c==15 or c == 16): sum += c
  return sum
