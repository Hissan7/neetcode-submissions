class Solution:
    def topKFrequent(self,nums, k):

        frequencies = {}

        for number in nums:
            if number not in frequencies:
                frequencies[number] = 1
            else:
                frequencies[number] += 1

        result = []

        for i in range(k):

            highest_key = None
            highest_freq = 0

            for key in frequencies:

                if frequencies[key] > highest_freq:

                    highest_freq = frequencies[key]
                    highest_key = key

            result.append(highest_key)

            del frequencies[highest_key]

        return result