# Put your code here
def isSorted(list):
    x = 0
    if len(list) < 2:
        return True
    else:
        while x < (len(list)-1):
            if list[x] > list[x+1]:
                return False
            x += 1
        return True
# A main for testing your code
def main():
    lyst = [1,2,5,4,5,6]
    print(isSorted(lyst))
    #lyst = [1]
    #print(isSorted(lyst))
    #lyst = list(range(10))
    #print(isSorted(lyst))
    #lyst[9] = 3
    #print(isSorted(lyst))

if __name__ == "__main__":
    main()
