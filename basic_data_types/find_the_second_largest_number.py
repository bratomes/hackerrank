# Task:
# You are given N numbers. Store them in a list and find the second largest number.
#
# Input Format:
# The first line contains N. The second line contains an array A[] of N integers
# each separated by a space.
#
# Constraints:
# 2 <= N <= 10
# -100 <= A[i] <= 100
#
# Output Format
# Output the value of the second largest number.
#
# Sample Input
# 5
# 2 3 6 6 5
#
# Sample Output
# 5

N, A = int(input()), [int(i) for i in input().split()]
A.sort()
A.reverse()
for i in range(0, N):
    if A[i+1] < A[i]:
        print(A[i+1])
        break
