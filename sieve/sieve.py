def primes(limit):
    # create a dictionary where the keys are all the numbers from 2 up to the provided limit
    # all values are first set to None
    nums = dict.fromkeys(range(2, limit + 1))

    # continue looping through the dictionary until all values are either True (ie. prime) or False (ie. composite)
    while None in nums.values():
        # return the (key, value) pair for the first occurrence of None
        prime = next((k, v) for k, v in nums.items() if v == None)
        # set the flag for that key to be True (since we now know that it's prime)
        nums[prime[0]] = True

        # start checking the rest of the dictionary starting with the number after the one we just checked to be prime
        for keys in range(prime[0] + 1, limit + 1):
            # if the number has already been checked to be composite, skip it
            if nums.get(keys) == False:
                continue

            # if the number is a multiple of the prime we're checking, set the flag to be False
            if isMultiple(keys, prime[0]) == True:
                nums[keys] = False

    # return the list consisting of only the keys with the value True
    return [keys for keys in nums.keys() if nums.get(keys) == True]


def isMultiple(num_to_check, prime):
    while num_to_check > 0:
        num_to_check -= prime

    return num_to_check == 0

