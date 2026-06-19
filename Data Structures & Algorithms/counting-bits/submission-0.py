class Solution:
    def countBits(self,n: int) -> list[int]:
        """
        input is an integer
        1.) need to create a list that seperates the input number into a list of its +1 increments e.g 3 = [0,1,2,3] or 5 = [0,1,2,3,4,5]
        2.) iterate through the list and convert each number into its binary form
        3.) in each binary representation of the number, we count how many 1's are in the number
        4.) append that value to a new list 
        """
        range_list = []
        bin_list = []
        count_list = [0 for _ in range(n+1)]
        #print(count_list)
        for i in range(0,n+1): #iterates
            range_list.append(i) #creates the +1 increment list of the number e.g 3 = [0,1,2,3]
        for j in range_list: 
            bin_list.append(int(bin(j)[2:])) #create a new list bin_list and append the binary versions of the values of range_list to bin_list
        print(bin_list)
        for index,binary_value in enumerate(bin_list):
            #print(index,binary_value)
            for x in str(binary_value):
                if x == "1":
                    count_list[index] += 1
        return count_list

