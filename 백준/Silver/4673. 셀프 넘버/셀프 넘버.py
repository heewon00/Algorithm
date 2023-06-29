gen_num=set()
for i in range(1,10001):
    i += sum(int(j) for j in str(i))
    gen_num.add(i)

ttl_num = set(range(1,10001))
self_num = sorted( ttl_num - gen_num)
for i in self_num:
    print(i)