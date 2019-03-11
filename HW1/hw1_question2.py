#homework_org_1.2, Palindrome madness
def check_palindrome():
    """
    Runs through all 6-digit numbers and checks the mentioned conditions.
    The function prints out the numbers that satisfy this condition.

    Note: It should print out the first number (with a palindrome in its last 4 digits),
    not all 4 "versions" of it.
    """
    pal_num=set()
    for i in range(100000,1000000,1):
    #    con1=False
    #    con2=False
    #    con3=False
    #    con4=False
        num=i
    #The first number has a palindrome in its last 4 digits.  
        if str(num)[5]==str(num)[2] and  str(num)[4]==str(num)[3]:
            #con1=True
    #After adding 1, the result has a palindrome in its last 5 digts.
            num=num+1
            if str(num)[5]==str(num)[1] and  str(num)[4]==str(num)[2]:
               # con2=True
            # Another addition of 1 results in a palindrome in the middle 4 digits.
                num=num+1
                if  str(num)[4]==str(num)[1]  and  str(num)[3]==str(num)[2]:
                   # con3=True
                #A final addition of 1 results in a 6-digit palindrome.
                    num=num+1
                    if str(num)[5]==str(num)[0]  and  str(num)[4]==str(num)[1]  and  str(num)[3]==str(num)[2]:
                       # con4=True
                        # if con1==True and  con2==True and con3==True and con4==True :
                        pal_num.add(i)
                    

    return(pal_num)


if __name__ == '__main__':
    #Question 2
    return_value = check_palindrome()
    print(f"Question 2 solution: {return_value}")
