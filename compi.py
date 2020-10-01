# Give a non-empty array of integers every element appears twice except for one.Find the single elemnt


def array_list1(input):
    output = set()
    repeat = set()
    if len(input)<0:
        return print("It will ot work")

    for x in input:
        if x not in output:
            output.add(x)
        else:
            repeat.add(x)
    
    print(output-repeat)
    print(output)
    print(repeat)
x = array_list1([2,2,1])



    
