import sys

def findFrequentEntries(pairs):
  # Your code here. Writes to standard out.
  # Format for output lines: "Name: 1230 1240 1245"
    dict = {} 
    for element in pairs:
        if element[0] not in dict:
            dict[element[0]] = [int(element[1])]
        else:
            dict[element[0]] += [int(element[1])]
    res = {}
    new_dict = {}
    for key in dict.keys():
        if len(dict[key]) >= 3:
            new_dict[key] = dict[key].sort()
    new_dict = dict.keys()
    
    #print(dict)
    for key in dict.keys():
        for i in range(len(dict[key])-1):
            j = i+1
            temp = [dict[key][i]]
            #print(temp)
            while j < len(dict[key]) and dict[key][j] <= dict[key][i]+100:
                temp.append(dict[key][j])
                j += 1
            if j - i >= 3 and key not in res:
                res[key] = temp
            #print(temp)
    #print(res)        
    if not res:
      print("None")
    for element in res.keys():
        string = ""
        length = len(res[element])
        for i in range(length-1):
            string += str(res[element][i]) + " "
        string += str(res[element][length-1])
        print("{0}: {1}".format(element, string))
        
# DO NOT MODIFY BELOW THIS LINE
def main():
  pairs = []

  for line in sys.stdin:
    if len(line.strip()) == 0:
      continue

    line = line.rstrip()
    pairs.append(line.split(" "))

  findFrequentEntries(pairs)

main()
