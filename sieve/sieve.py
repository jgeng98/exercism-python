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

        # check the rest of the dictionary, starting at 2*prime[0] and incrementing by prime[0] each time
        # all those numbers will be a multiple of prime[0] by definition, so we can set their values to be False
        for keys in range(prime[0] * 2, limit + 1, prime[0]):
            nums[keys] = False

    # return the list consisting of only the keys with the value True
    return [keys for keys in nums.keys() if nums.get(keys) == True]
