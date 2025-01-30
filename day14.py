
# file IO operations - modes - create,read,write,append

'''

x - create
r - read
a - append
w - write

'''
#read
'''

r - reads content
rt - reads text content
rb - reads binary code

'''

# f = open('temp.txt','r')
# print(f)
# text = f.read()
# print(text)
# f.close()


# write 
'''

w - writes content 
wb - writes binary content  

'''

# file maker

# import os

# def fileMaker():
#     for day in range(14,20):
#         with open(f'day{day+1}.py', 'x') as f:
#             pass
# fileMaker() 




# i = 0
# f = open('temp1.txt', 'r')

# while True:
#     i += 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(',')[0]
#     m2 = line.split(',')[1]
#     m3 = line.split(',')[2]

#     print(f'marks of student {i} of sub1 is: {int(m1)}')
#     print(f'marks of student {i} of sub1 is: {int(m2)}')
#     print(f'marks of student {i} of sub1 is: {int(m3)}')
# print(line)


# readline, readlines,

#readline - takes only one line,
#readlines - # returns (reads) the list of lines


# readlines
# reads line with an Iterable object
# with open('D:/Cognisun/Python/temp.txt','r') as l:
#     line = l.readlines() 
# print(line)

#writelines
# writes iterable objects in file
# with open('D:/Cognisun/Python/temp.txt', 'w') as l:
#     lines = ['Line 1\n', 'Line 2\n', 'Line 3']
#     l.writelines(lines)
    
    
#write

# with open('temp2.txt', 'w') as l:
#     lines = ['Line 1', 'Line 2', 'Line 3', 'Line 4', 'Line n']
    
#     for line in lines: 
#         l.write(line + '\n')
