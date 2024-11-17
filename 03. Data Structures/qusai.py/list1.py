# list1 = [1,2,3,4,5,32]
# print(len(list1))
# print(max(list1))
# print(min(list1))
# print(sum(list1))
# import random
# random.shuffle(list1)

#nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn

# list1 = [2,3]
# list2 = [1,9]
# list3 = list1 + list2
# print(list3)
# list3 = 2*list1
# print(list3)
# list4 = list3[2:4]
# print(list4)

#tttttttttttttttttttttttttttttttttttttttttttttttttt

# list1= [2,3,5,2,33,21]
# list1[-1]
# print(list1[-1])

#33333333333333333333333333333333333333333333333333

# list1 =[2,3,5,2,33,21]
# i = 0 
# while i < len(list1):
#     print(list1[i],end=" ")
#     i += 1

#44444444444444444444444444444444444444444444444444

# list1 =[x for x in range (0,5)]
# print (list1)

# list2 = [0.5*x for x in list1]
# print(list2)

# list3 = [x for x in list2 if x <1.5]
# print(list3)

#5555555555555555555555555555555555555555555555555

# list1 =["pink","red","blue" ]
# list2 =["green","red and" ,"blue","green"]
# print(list1 == list2) 
# print(list1!= list2)
# print(list1>= list2)
# print(list1> list2)
# print(list1< list2)
# print(list1<= list2)

#66666666666666666666666666666666666666666666666666

# items ="Welcome to the SCME".split()
# print(items)
# items ="34#13#78#45".split("#")
# print(items)

#================ new day ============================================ new day ====================================================== new day ================================
#                                      2024\11\10                                                   2024\11\10                                                               =
#================ new day ============================================ new day ====================================================== new day ================================

# def reverse(list):
#     result = []
#     for element in list :
#         result.insert(0,element)
#     return result


# list1 =[1,2,3,4,5,6]
# list2 =reverse(list1)
# print (list2)
#===================================================

# list3 =[10,20,30,40,50,60]
# list3.reverse()
# print (list3)

#222222222222222222222222222222222222222222222222222

#def  linearshearch(lst,key):
#     for i in range(0,len(lst)):
#         if key == list[i]:
#             return i
#     return -1
# list =[2,3,4,5]
# print(linearshearch(list,5))

##================ new day ============================================ new day ====================================================== new day ===============================
#                                      2024\11\12                                                   2024\11\12                                                               =
#================ new day ============================================ new day ====================================================== new day ================================

# def selectionsort(lst):
#     for i in range(len(lst) - 1):
#         currentMin = min(lst[i: ])
#         currentMinIndex = i + lst[i: ].index(currentMin)
#         if currentMinIndex != i:
#             lst[currentMinIndex], lst[i] = lst[i], currentMin
#     return lst
# lest4 = [4,5,99,8,9]
# selectionsort(lest4)
# print(lest4)

#222222222222222222222222222222222222222222222222

# list2=[1,2,5,6,8,5,99,0]
# list2.sort()
# print(list2)

##================ new day ============================================ new day ====================================================== new day ===============================
#                                      2024\11\17                                                   2024\11\17                                                               =
#================ new day ============================================ new day ====================================================== new day ================================ 

# total = 0
# import random
# matrix =[]
# numberOFcolumns =eval(input("Enter the number of colums: "))
# numberOFRows =eval(input("Enter the number of Rows: "))
# for row in range(0,numberOFRows):
#     matrix.append([])
#     for column in range(0,numberOFcolumns):
#         matrix[row].append(random.randrange(0,100))
#         total  +=matrix[row][column]
                          
# print("Total is 2 is" + str(total))
# print(matrix)

#222222222222222222222222222222222222222222222222

#matrix=[]
# NumOfRows=eval(input("Enter the number of rows : "))
# NumOfcols=eval(input("Enter the number of cols : "))

# for row in range(0,NumOfRows):
#     matrix.append([])
#     for Cols in range(0,NumOfcols):
#         print("Row#",row+1 , " Cloumn# " , colum +1)
#         value=eval(input("Enter the element and enter "))
#         matrix[row].append(value)
# print(matrix)