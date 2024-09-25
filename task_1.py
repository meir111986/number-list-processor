def get_numbers():
    numbers = input("Введите числа, разделенные пробелами: ").split()
    arr = []
    for num in numbers:
        arr.append(int(num))
    print(arr)
    return arr

def process_numbers(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    avg_num = sum(numbers) / len(numbers)
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    
    print(f"Наибольшее число: {max_num}")
    print(f"Наименьшее число: {min_num}")
    print(f"Среднее арифметическое: {round(avg_num, 2)}")
    print(f"Четные числа: {even_numbers}")

numbers = get_numbers()
process_numbers(numbers)
