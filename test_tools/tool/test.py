


import sys
# data = sys.argv[0]
# data2 = sys.argv.remove(data)
# list = []
print(sys.argv)
list = str(sys.argv[1]).split(';')
# print(list)
for i in list:
    list2= str(i).split(',')
    # print(list2)
    if len(list2) >1:
        print(list2)
        for j in list2:
            print(j)
        # method = list2[0]
        # url = list2[1]
        # data = list2[2]
        # print(method,url,data)
# print(len(sys.argv))
# for i in sys.argv:
#     print(i)
    # print(str(i).replace('\"','').strip(',').strip('[)').strip(')]'))

# print(list)