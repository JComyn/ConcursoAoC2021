with open("input.txt") as f:
    numbers = f.readlines()
numbers_copy = numbers.copy()

#Oxygen generator rating
for i in range(12):
    if len(numbers) > 1:
        count0 = 0
        count1 = 0
        for number in numbers:
            if number[i] == '0':
                count0 += 1
            else:
                count1 += 1
        for number in numbers[:]:
            if number[i] == '0' and count1 >= count0:
                numbers.remove(number)
            if number[i] == '1' and count0 > count1:
                numbers.remove(number)
oxygen = int(numbers[0], 2)

#C02 scrubber rating
for i in range(12):
    if len(numbers_copy) > 1:
        count0 = 0
        count1 = 0
        for number in numbers_copy:
            if number[i] == '0':
                count0 += 1
            else:
                count1 += 1
        for number in numbers_copy[:]:
            if number[i] == '0' and count1 < count0:
                numbers_copy.remove(number)
            if number[i] == '1' and count0 <= count1:
                numbers_copy.remove(number)

co2 = int(numbers_copy[0], 2)
print(co2 * oxygen)
