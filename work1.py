log_list = []
with open ('test.txt', mode = 'r', encoding = 'utf=8') as f:
  i = 0
  for i, s in enumerate(f, start = 0):
    log_list.append(s.rstrip().split(','))
  
  i = 0
  c = 0
  check = []
  for c in range(c, len(log_list)):
    check.append(0)
  
  for i in range(i, len(log_list)):
    if(log_list[i][2] == '-'):
      for j in range(i+1, len(log_list)):
        if(log_list[i][1] == log_list[j][1] and log_list[j][2] == '-'):
          continue
        if(log_list[i][1] == log_list[j][1] and log_list[j][2] != '-' and check[j] == 0):
          print(log_list[i][0] + '~' + log_list[j][0])
          check[j] = 1
          break


