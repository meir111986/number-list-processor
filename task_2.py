elements = input("Введите элементы списка через пробел: ").split()
k = int(input("Введите количество позиций для сдвига: "))

shifted_list = ''
direction = ''
n = len(elements)
k = k % n
if k > 0:
    shifted_list = elements[-k:] + elements[:-k]
    direction = 'вправо'
else:
    shifted_list = elements[-k:] + elements[:-k]
    direction = 'влево'

print(f"Результат сдвига:{direction}", " ".join(shifted_list))
