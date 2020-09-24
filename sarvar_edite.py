def remove_lowercase(string1, string2):
    str1 = open(string1)
    str2 = open(string2,'w')
    for line in str1.readlines():
        if line[0] != line[0].lower():
            str2.write(line)
    str2.close()
    print(open(string2).read())


remove_lowercase('sample.txt', 'sample3.txt')
