def unique_combinations(nums, target):
    """Return the first expression using any number of the input values."""

    def search(numbers, expressions):
        # Stop immediately if any current value reaches the target.
        for number, expression in zip(numbers, expressions):
            if abs(number - target) < 1e-9:
                return expression

        # No more operations can be made, and the target was not reached.
        if len(numbers) == 1:
            return ""

        # Try every pair of current numbers.
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                a, b = numbers[i], numbers[j]
                expression_a, expression_b = expressions[i], expressions[j]

                # Keep the numbers and expressions that were not selected.
                remaining_numbers = [
                    number for k, number in enumerate(numbers)
                    if k != i and k != j
                ]
                remaining_expressions = [
                    expression for k, expression in enumerate(expressions)
                    if k != i and k != j
                ]

                # Store every valid operation and its expression.
                combinations = [
                    (a + b, f"{expression_a}+{expression_b}"),
                    (a - b, f"{expression_a}-{expression_b}"),
                    (b - a, f"{expression_b}-{expression_a}"),
                    (a * b, f"{expression_a}*{expression_b}"),
                ]

                if b != 0:
                    combinations.append(
                        (a / b, f"{expression_a}/{expression_b}")
                    )
                if a != 0:
                    combinations.append(
                        (b / a, f"{expression_b}/{expression_a}")
                    )

                # Try each operation and search again with its result.
                tried = set()
                for result, expression in combinations:
                    # Avoid trying the same result more than once.
                    state = (result, expression)
                    if state in tried:
                        continue
                    tried.add(state)

                    solution = search(
                        remaining_numbers + [result],
                        remaining_expressions + [expression],
                    )
                    if solution:
                        return solution

        # None of the possible operations reached the target.
        return ""

    # Start with each input number and its string representation.
    return search(list(nums), [str(number) for number in nums])


nums = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
target = int(input("Enter the target number: "))
solution = unique_combinations(nums, target)
print(solution if solution else "cant find a unique sol")
