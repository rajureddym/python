num_list= [1,23,567,34567,900,11]
print(min(num_list))
print(max(num_list))


sum=0
for i in range(len(num_list)):
    sum=sum+num_list[i]

avg=sum/len(num_list)
print('The sum & avegrage is',sum,avg)

for i in range(len(num_list)):
    if num_list[i]>=avg:
        print(num_list[i])