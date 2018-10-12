def string_bits(str):
  string = ""
  for i in range(len(str)):
    if(not i&1): string+=str[i]
  return string
