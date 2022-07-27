def prng_compute(pattern,update_rule):
    
    j = bin(update_rule).replace('0b','').zfill(8)
    m = list(j)
    for l in range(len(m)):
        m[l] = int(m[l])
    my_update_rule = m

    j = bin(pattern).replace('0b','').zfill(32)
    m = list(j)
    for l in range(len(m)):
        m[l] = int(m[l])
    my_pattern = m

    my_pattern_new = [0 for i in range(32)]

    k = my_pattern[-1:] + my_pattern[0:2]
    for l in range(len(k)):
        k[l] = str(k[l])
    k = int(''.join(k),2)
    my_pattern_new[0] = my_update_rule[k]

    for i in range(30):
        k = my_pattern[i:i+3]
        for l in range(len(k)):
            k[l] = str(k[l])
        k = int(''.join(k),2)
        my_pattern_new[i+1] = my_update_rule[k]

    k = my_pattern[30:32] + my_pattern[0:1]
    for l in range(len(k)):
        k[l] = str(k[l])
    k = int(''.join(k),2)
    my_pattern_new[31] = my_update_rule[k]

    for l in range(len(my_pattern_new)):
        my_pattern_new[l] = str(my_pattern_new[l])
    return int(''.join(my_pattern_new),2)
  






