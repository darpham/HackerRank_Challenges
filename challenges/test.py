# import sys

# maj_ver = sys.version_info.major  
# print(maj_ver)

# print(sys.version_info)


# if False:
#     print(1)
# elif True:
#     print(2)
# else:
#     print(3)

# test = ['a', 'b', 'c']

# arr = ['a', 'a', 'c']

# # if (x,y,z) in test:
# #     print('true')

# if all(arr in test):
#     print('true')


# x = [1]

# if 1 in range(2,5):
#     print('true')
# else:
#     print('false')

# if 6 in range(2,6):
#     print('true')

def oddNumbers(l, r):
    output = []
    for i in range(l, r+1):
        if i % 2 != 0:
            output.append(i)
    
    return(output)

print(oddNumbers(2,5))