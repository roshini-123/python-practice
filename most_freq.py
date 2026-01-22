def most_freq_num(num_list):
    freq = {}
    for n in num_list:
        if n not in freq:
            freq[n] = 1
        else:
            freq[n] = freq[n] + 1

    max_number = max(freq.values())

    result = [num for num,count in freq.items() if count == max_number]        

    print("result",result)     


num_list = [1,1,2,2,2,2,4,4,4,4,5,5]

most_freq_num(num_list)
