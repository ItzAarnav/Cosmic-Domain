print("Stat Calc")

switch = True

while switch:
    numbers = input("[NOTE: YOU WILL BE PROMPTED THIS FOREVER]Enter your numbers seprated by a space > ").split(" ")
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[i]:
                numbers[j], numbers[i] = numbers[i], numbers[j]
    try:
        numbers = [int(i) for i in numbers]

        # Mean
        sum = 0
        for i in numbers:
            sum += i
        mean = round(sum / len(numbers), 2)

        # Least and Greatest
        least = numbers[0]
        greatest = numbers[len(numbers) - 1]

        # Median
        mnumbers = numbers.copy()
        median = 0

        mediated_numbers = [i for i in mnumbers]

        while len(mediated_numbers) != 2 or len(mediated_numbers) != 1:
            del mediated_numbers[0], mediated_numbers[len(mediated_numbers) - 1]
            if len(mediated_numbers) <= 2:
                break

        if len(mediated_numbers) == 2:
            median = (mediated_numbers[0] + mediated_numbers[1]) / len(mediated_numbers)
        else:
            median = mediated_numbers[0]

        # Output
        print(f"Mean: {mean}\nMedian: {median}")
        print(f"Least: {least}\nGreatest: {greatest}")

        queries = - 1
    except:
        print("There is an invalid value in your list, please try again.")
