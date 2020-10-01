def merge_the_tools(string, k):
    if len(string)<0:
        return False
    target = len(string)//k
    for x in range(0,len(string),target):
        result = string[x:x+target]
        final = ""
        for y in result:
            if y not in final:
                final+=y
        print(final)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)