def christmastree(height,symble):
    for i in range(1,height+1):
        print(" "*(height-i) + symble*(2*i-1))


heights=int(input("enter the  height:"))
symbles=input("enter a symble *, & ,% ,...")
christmastree(heights,symbles)
    