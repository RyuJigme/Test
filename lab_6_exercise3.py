for num in range(1, 8):
  if num == 7:
    break
  for inner_num in range(1, 8):
    if inner_num == 3:
      continue
    print(inner_num, end=" ")
  print()  