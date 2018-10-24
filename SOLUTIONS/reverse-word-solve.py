def reverseword():
    s=input("Type the String:")
    temp_=s.split(" ")
    finalstr=""
    for i in range(len(temp_)):
        finalstr+=temp_[len(temp_)-1-i]
        finalstr+=" "
    print(finalstr)
