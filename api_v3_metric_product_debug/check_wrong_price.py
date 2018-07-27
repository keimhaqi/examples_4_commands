file = open("/home/zhenping/github/examples_4_commands/api_v3_metric_product_debug/prices")
sum_price = 0
count = 0
for line in file:
    string = line.replace('\n', '').split("=")
    sum_price = sum_price + float(string[1])
    count = count + 1

print("count = " + str(count))
print("sum_price = " + str(sum_price))
print("average = " + str(sum_price / count))
        
