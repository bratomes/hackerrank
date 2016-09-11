# Task:
# Now, let's use our knowledge of sets and help Mickey.
# Ms. Gabriel Williams is a botany professor at District College.
# One day, she asked her student Mickey to compute the average of
# all the plants with distinct heights in her greenhouse.
#
# Formula used:
# Average = sum of distinct heights / total number of distinct heights
#
# Input Format:
# The first line contains the integer, N, the total number of plants.
# The second line contains the  space separated heights of the plants.
#
# Constraints:
# 0 < N <= 100
#
# Output Format:
# Output the average height value on a single line.
#
# Sample Input
# 10
# 161 182 161 154 176 170 167 171 170 174
#
# Sample Output
# 169.375

N = int(input())
plants_heights = input().split()

sum_distinct_heights = sum(int(plant_height) for plant_height in set(plants_heights))
len_distinct_heights = len(set(plants_heights))

average = sum_distinct_heights / len_distinct_heights

print(average)

