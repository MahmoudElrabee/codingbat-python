def caught_speeding(speed, is_birthday):
  if(is_birthday):
    if(speed > 65 and speed <= 86):return 1
    elif(speed <= 65):return 0
    else:return 2
  elif(speed <= 60):return 0
  elif(speed>=61 and speed<=80):return 1
  else:return 2

