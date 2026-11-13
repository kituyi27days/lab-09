# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline:
    ''' Loop through the whole list, 
    then use another loop to loop through the the next item in the list, 
    then add the two numbers you get by the two different loops and check againt target, 
    then also make sure the second loop in iside the first loop so that 
    it will chech the first item against everthing else in the list 
    and so on so fourth till everything in the list has been checked. '''
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def max_profit(prices):
    # Outline:
    ''' get the lowest so far, get the maximum proft (it is zero initialy), 
    loop through each price, 
    If the current price is lower than our minimum price change the lowest price, 
    calculate the profit we would make by selling at the current price, 
    If that profit is greater than our previous maximum profit change it, 
    return the maximum profit. '''

    if not prices:
        return 0

    min_price = prices[0]
    max_profit_value = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price

            if profit > max_profit_value:
                max_profit_value = profit

    return max_profit_value


def max_subarray(nums):
    # Outline:
    '''assume first number is largest sum, 
    two variables needed current_sum and max_sum, 
    loop through remaining numbers, when your at each number add 
    to the previous subarray and start a new subarray from the current number, 
    update max_sum whenever a larger sum is found'''

    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    '''Create an empty stack and a dictionary to match brackets, 
    loop through the string and add opening brackets to the stack, 
    when a closing bracket appears check if it matches the last opening bracket, 
     return False if it does not match or the stack is empty, 
    return True if the stack is empty at the end otherwise return False'''
    stack = []

    matching = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        if char in "([{":
            stack.append(char)

        elif char in matching:
            if not stack:
                return False

            last_open = stack.pop()

            if last_open != matching[char]:
                return False

    return len(stack) == 0


def main():
    two_sum([2, 7, 11, 15], 9)   # returns [0, 1]   (2 + 7)
    two_sum([3, 2, 4], 6)  
    
    max_profit([7, 1, 5, 3, 6, 4])   # returns 5   (buy at 1, sell at 6)
    max_profit([7, 6, 4, 3, 1])      # returns 0   (prices only fall)


    max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])  # returns 6   (4 + -1 + 2 + 1)
    max_subarray([5, 4, -1, 7, 8])  # returns 23  (the whole list)       
    
            
if __name__ == "__main__":
    main()
