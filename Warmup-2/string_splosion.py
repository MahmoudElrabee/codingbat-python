def string_splosion(str):
  string = ""
  for i in range(len(str)+1):
    string += str[0:i]
  return string

