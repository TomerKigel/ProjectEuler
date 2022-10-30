def comparedicts(dict1,dict2):
    for key1 in dict1:
        if key1 != 'elem':
            if key1 not in dict2:
                return False
            else:
                if dict2[key1] != dict1[key1]:
                    return False
    for key2 in dict2:
        if key2 != 'elem':
            if key2 not in dict1:
                return False
    return True


def count_dicts(list_of_dicts):
    smallest_elem = 0
    max_count = 0
    for dict1 in list_of_dicts:
        count = 0
        for dict2 in list_of_dicts:
            if dict1 != dict2:
                if comparedicts(dict1,dict2):
                    count += 1
                    if count > max_count:
                        smallest_elem = dict1['elem']
                        max_count = count
    return smallest_elem

if __name__ == '__main__':
  lst = []
  i = 100
  while i < 10000:
      lst.append(i**3)
      i += 1
  listOfDicts = []
  for elem in lst:
      t_d = {'elem' : elem}
      elem = str(elem)
      for ch in elem:
          if int(ch) in t_d:
            t_d[int(ch)] += 1
          else:
            t_d[int(ch)] = 1
      listOfDicts.append(t_d)
  print(count_dicts(listOfDicts))