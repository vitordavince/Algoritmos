def quickshort(array):
  if len(array) < 2:
    return array
  else:
    pivo = array[0]
    menores = [i for i in array[1:] if i <= pivo]
    maiores = [i for i in array[1:] if i > pivo]
    return quickshort(menores) + [pivo] + quickshort(maiores)

print(quickshort([10, 5, 2, 3]))