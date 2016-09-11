# Initialize your list and read in the value of n followed by n lines of commands
# where each command will be of the 7 types listed above. Iterate through each
# command in order and perform the corresponding operation on your list.
#
# Input Format
# The first line contains an integer, n, denoting the number of commands.
# Each line i of the n subsequent lines contains one of the commands described above.
#
# Constraints
# The elements added to the list must be integers.

# Output Format
# For each command of type print, print the list on a new line.
#
# Sample Input
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample Output
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

l = []
n = int(input())

for i in range(1, n + 1):
    command = input().split()
    if command[0].startswith('print'):
        print(l)
        continue
    command = 'l.{}({})'.format(command[0], ', '.join(command[1:]))
    eval(command)
