import numpy as np
matrix = np.array([[14, 21, 213, 188, 171, 78, 155, 155, 148, 40],
                   [110, 100, 185, 254, 243, 139, 113, 68, 9, 7],
                   [119, 81, 97, 228, 134, 143, 60, 6, 83, 34],
                   [130, 255, 172, 46, 228, 203, 188, 232, 195, 202],
                   [90, 251, 246, 41, 193, 183, 118, 135, 125, 236],
                   [128, 212, 90, 226, 230, 118, 145, 235, 185, 124],
                   [56, 83, 179, 42, 232, 68, 233, 79, 245, 180],
                   [129, 132, 166, 150, 79, 53, 131, 239, 159, 19],
                   [210, 185, 232, 48, 190, 15, 167, 69, 58, 224],
                   [27, 133, 218, 62, 53, 225, 108, 183, 8, 92]])


filter = np.array([[-0.7, 0.4, -0.9],
          [1.0, -1.0, 0.5],
          [-1.0, -0.5, 0.7]])


res = []
res1 = []
res2 = []
width = len(matrix[0])
length = len(matrix)
i = 1
j = 1

for i in range(length - 1):  # разделяем матрицу на части
    output_list = []
    output_list1 = []
    output_list2 = []
    for j in range(width - 1):
        v = np.array(matrix[i - 1:i + 2, j - 1:j + 2])
        if v.size != 0:
            output_list.append(np.sum(v.dot(filter)).round(1))
            output_list1.append(np.max(v.dot(filter)).round(1))
            output_list2.append((np.sum(v.dot(filter)) / 9).round(1))
    res.append(output_list)
    res1.append(output_list1)
    res2.append(output_list2)


    i += 1
    j += 1
print("сумма")
for i in range(1, len(res)):
    print(res[i])
print("\n")
print("максимум")
for i in range(1, len(res1)):
    print(res1[i])
print("\n")
print("среднее")
for i in range(1, len(res2)):
    print(res2[i])
