# put your code here
num = int(input())
sum_ = 0
count = 0
while num != 55:
    sum_ += num
    count += 1
    num = int(input())

average = round(sum_ / count)

print(count)
print(sum_)
print(average)
