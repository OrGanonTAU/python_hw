#homework_org_1.1
def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    count=0
    skip=False
    for i in range(0,len(word)-1):
        if skip==True: 
            skip=False
            pass
        else:
            if word[i]==word[i+1]:
                count+=1 #add 1 to count
                skip=True
                if count==3:
                    return True 
            else:
                count=0
                skip=False
            #print (count)
    return False


if __name__ == '__main__':
    #Question 1
    myword = 'gbbccff'
    return_value = trifeca(myword)
    print('Question 1 example input: ',myword)
    print(f"Question 1 solution: {return_value}")
