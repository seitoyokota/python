def main():
    nums = input("numbers: ").split()
    total = 0
    average = 0
    real_num_cnt = 0
    missing_location = []
    for i in range(len(nums)):
        if(int(nums[i])==-1):
            missing_location.append(i)
        else:
            total += int(nums[i])
            real_num_cnt += 1
    for i in range(len(missing_location)):
        average = total//real_num_cnt
        nums[missing_location[i]] = average
    print(nums)

if __name__ == "__main__":
    main()