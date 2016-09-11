# Task
# Given  sets of integers, M and N, print their symmetric difference in ascending order.
# The term symmetric difference indicates those values that exist in either M or N but do not
# exist in both.
#
# Input Format
# The first line of input contains an integer, M.
# The second line contains M space-separated integers.
# The third line contains an integer, N.
# The fourth line contains N space-separated integers.
#
# Output Format
# Output the symmetric difference integers in ascending order, one per line.
#
# Sample Input
# 4
# 2 4 5 9
# 4
# 2 4 11 12

# Sample Output
# 5
# 9
# 11
# 12

m, m_set = int(input()), set(input().split())
n, n_set = int(input()), set(input().split())

values_in_m = m_set.difference(n_set)
values_in_n = n_set.difference(m_set)

m_union_n = values_in_m.union(values_in_n)

for number in sorted(int(i) for i in m_union_n):
    print(number)
