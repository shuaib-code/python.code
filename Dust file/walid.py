def cal(x=None):
    if isinstance(x, int):
        dic_result = {"Stamp":abs(x*15-100),"Ragi":x*10+388,"Sun Ragi":x*30,"SR":x*20}
        for dic_Key in dic_result:
            print(f"{dic_Key}: {dic_result[dic_Key]}")
    else:
        print("Please enter a valid integer value for X.")
cal(int(input("Enter the value of X: ")))