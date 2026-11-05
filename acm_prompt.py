def main():
    nums = input("numbers: ").split()
    mode = []
    counter = 0
    popular = 0
    populars = []
    temp = 0
    most_popular = True
    for i in range(len(nums)):
        counter = 0
        for num in nums:
            if(nums[i]==num):
                counter += 1
        mode.append(counter)
    for i in range(len(nums)):
        most_popular = True
        for j in range(len(nums)):
            if(mode[i]<mode[j]):
                most_popular = False
        if(most_popular==True):
            populars.append(nums[i])
    populars.sort()
    print(populars[0])
        

if __name__ == "__main__":
    main()