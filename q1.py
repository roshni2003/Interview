# list1 = [1,2,3,4,5]
# list2 = [3,5,8,1,6]
# i=0
# list=[]
# while i<len(list1):
#     list.append(list1[i]*list2[i])
#     i+=1
# print(list)



# Name	Age
# A	10
# B	23
# C	34
# D	44
# E	12
# F	9

# dict=[{'Name':'A','Age':10},{'Name':'B','Age':23},{'Name':'C','Age':34},{'Name':'D','Age':44},{'Name':'E','Age':12},{'Name':'F','Age':19}]
# for i in dict:
#     if i["Age"]<25:
#         print("young")
#         i["type"]="young"
#     if i["Age"]>25 and i["Age"]<40:
#         print("middle age")
#         i["type"]="middle age"
#     if i["Age"]>40:
#         print("old age")
#         i["type"]="old age"
        
# print(dict)


# range1 = '15-30'
# list=[]
# a=range1.split("-")
# for i in range(int(a[0]),int(a[1])+1):
#     # if range(int(a[1]))<30:
#         list.append(i)
# print(a)


# list=[1,2,3,4,1,2,3]
# i=0
# list1=[]
# while i<len(list):
#     if list[i] not in list1:
#         list1.append(list[i])
#     i=i+1
# print(list1)

# a="1"
# b="monika"
# c="5.4"
# t=float(c)
# u=int(a)
# print(b,t+u)
# # print(i)



T = int(input())
for i in range(T):
    num = int(input())
    def func (List):
        c = 0
        num1 = List[0]
         
        for i in List:
            tech = List.c(i)
            if(tech>c):
                c = tech
                num = i
     
        if c>=3:
            print("NO")
        else:
            print("YES")
        
    a = list(map(int,input().split()))
    func(a)
    
    

# def min_colors(n, k): 
#     if k <= 1: 
#         return k 
#     if n <= k: 
#         return n 
#     c = [0] * k 
#     for i in range(1, k+1): 
#         c[i-1] = i 
#     for i in range(k+1, n+1): 
#         for j in range(1, k+1): 
#             t = c[j-1] 
#             if t > c[i-j-1]: 
#                 t = c[i-j-1] 
#             c[j-1] = t + 1
#     return c[k-1] 
# n, k = map(int, input().split())
# print(min_colors(n, k)

         
        