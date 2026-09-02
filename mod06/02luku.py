
numbers = []

while True:
    input_number = input("Anna luku: ")
    if input_number == "":
        break
    numbers.append(int(input_number))
numbers.sort(reverse=True)
        
for num in range(5):
    print(numbers[num])
    
