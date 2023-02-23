import statistics, hello_module
nums = [32,3, 546, 2, 1 ,4, 673, 482037, 28, 57767, 28348, 2]
mean = statistics.mean(nums)
median = statistics.median(nums)
mode = statistics.mode(nums)

print(hello_module.cubed(3))
print("mean:", mean, "\nmedian:", median, "\nmode:", mode, )

hello_module.print_hello()