# Last updated: 7/17/2025, 4:58:26 PM
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        result = []

        for i in range(1, n + 1):
            output = ""

            if i % 3 == 0:
                output += "Fizz"
            if i % 5 == 0:
                output += "Buzz"

            if output == "":
                output = str(i)

            result.append(output)

        return result
"""
        result = []

        for i in range(1, n + 1):
            output = ""

            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result

"""