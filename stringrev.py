
def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    a =""
    for x in sentence:
        if x.isupper() ==True:
            a+=(x.lower())
        else:
            a+= (x.upper())
    result = a.split(' ')
    final = ' '.join(reversed(result))
    return final