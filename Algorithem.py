# # getting 10 numbers from user and additional it in list and print it

# numbers_by_user = []

# for i in range(10):
#     num = input("enter your number to store it in list: ")
#     numbers_by_user.append(num)

# print(numbers_by_user)





## 1-factorial # work

# # iterative
# def factorial(n):
#     f = 1
#     i = n
#     while i > 0:
#         f = f * i
#         i -= 1
#     return f
# print(factorial(5))

# # recursive
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))





# # 2-linear search(iterative, recursive)    # work

# def linear_search_iterative(a, n, key):
#     i = 0
#     while i < n:
#         if a[i] == key:
#             return i
#         else:
#             i += 1
#     if i == n:
#         return -1
    
# n = 10
# data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# key = int(input("please value to be located: "))

# location = linear_search_iterative(data, n, key)

# if location == -1:
#     print("not located in data")
# else:
#     print(f"{key} is located at position", location)


# def linear_search_recursive(a, n, key):
        
#         if n == 0:
#             return -1
#         else:
#             if a[n-1] == key:
#                 return n-1
#             else:
#                 return linear_search_recursive(a, n-1, key)
            
# n = 10
# data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# key = int(input("please value to be located: "))

# location = linear_search_recursive(data, n, key)
# if location == -1:
#     print(f"{key} not located in data")
# else:
#     print(f"{key} is located at position", location)






# # 2- Binary search(iterative, recursive)

# def binary_search(key):
#     list2 = [10,20,30,40,50,60,70,80,90,100]
#     lower = list2[0]
#     upper = list2[-1]

#     while lower <= upper:
#         if lower > upper:
#             print("x does not exists")
#             break
#         mid = (lower + upper) // 2

#         if mid < key:
#             lower = mid + 1
#         elif mid > key:
#             upper = mid - 1
#         else: # mid == key
#             print(f"{key} found at location {list2.index(key)}")
#             break

# binary_search(90)


# def binary_search_recursive(a, start, end, key):
#     if start <= end:
#         mid = (start+end) / 2
#     else:
#         return -1
    
#     if key == a[mid]:
#         return mid
#     else:
#         if key > a[mid]:
#             return binary_search_recursive(a, mid+1, end, key)
#         else:
#             return binary_search_recursive(a, start, mid-1, key)

# key = float(input("please value to be located: "))
# data = [10.0,20.0,30.0,40.0,50.0,60.0,70.0,80.0,90.0,100.0]
# lower = 0
# upper = 9    # n-1

# pos = binary_search_recursive(data, lower, upper, key)

# if pos == -1:
#     print(f"{key} not located in data")
# else:
#     print(f"{key} is located at position", pos)











