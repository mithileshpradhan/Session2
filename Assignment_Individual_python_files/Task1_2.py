## ['A', 'C', 'A', 'D', 'G', 'I', 'L', 'D']

input_word1 = "ACADGILD"

output_list1 = [a for a in input_word1]
print("The output is :",output_list1)


## ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'] 

input_word2 = "xyz"
input_word2 = list(input_word2)  # ['x','y','z']
output_list2 = [num*a for a in input_word2 for num in range(1,5)]
print("The output is :",output_list2)



## ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz'] 
input_word3 = "xyz"
input_word3 = list(input_word3)  # ['x','y','z']
output_list3 = [num*a for num in range(1,5) for a in input_word3]
print("The output is :",output_list3)




## [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
input_word4 = "234"
input_word4 = [int(digit) for digit in input_word4]  # [2,3,4]
output_list4 = [ [item+num] for item in input_word4 for num in range(0,3)]
print("The output is :",output_list4)





## [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]] 
input_word5 = "2345"
input_word5 = [int(digit) for digit in input_word5]  # [2,3,4,5]
output_list5 = [ [item+num for item in input_word5] for num in range(0,4)  ]
print("The output is :",output_list5)






## [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)] 
input_word6 = "123"
input_word6 = [int(digit) for digit in input_word6]   # [1,2,3]
output_list6 = [ (b,a) for a in input_word6 for b in input_word6]
print("The output is :",output_list6)

