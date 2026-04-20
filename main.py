import random

# 1. Створюємо двовимірний масив 3x3 з випадкових цілих чисел від 1 до 100
matrix = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]

print("Початковий масив:")
for row in matrix:
    print(row)

# 2. Обчислюємо суму всіх елементів масиву
total_sum = sum(sum(row) for row in matrix)
print("\nСума всіх елементів:", total_sum)

# 3. Знаходимо максимальне та мінімальне значення, а також їхні індекси
max_value = matrix[0][0]
min_value = matrix[0][0]
max_index = (0, 0)
min_index = (0, 0)

for i in range(3):
    for j in range(3):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_index = (i, j)
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            min_index = (i, j)

print("Максимальний елемент:", max_value, "Індекс:", max_index)
print("Мінімальний елемент:", min_value, "Індекс:", min_index)

# 4. Сортуємо кожен рядок масиву
sorted_matrix = [sorted(row) for row in matrix]

print("\nМасив після сортування кожного рядка:")
for row in sorted_matrix:
    print(row)