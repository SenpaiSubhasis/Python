def ask_ok(prompt,retries = 4, remainder = "Please Try Again"):
    while True:
        ok = input(prompt)
        if ok in ('y' , 'yes' , 'ye'):
            return True
        if ok in ('no' , "nop" , 'nope'):
            return True
        retries = retries -1
        if retries<0:
            raise ValueError("FUck off")
        else:
            print(remainder)

x = ask_ok("yes")
