def round_sum(a, b, c):
  def round10(n):
    if(n%10>=5):return n+10-n%10
    else:return n-n%10
  return round10(a)+round10(b)+round10(c)

