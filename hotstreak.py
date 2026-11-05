def main():
    temps = input("list temps seperated by spaces: ").split()
    streak=0
    longest_streak=0
    for i in range(len(temps)-1):
        if(temps[i]<temps[i+1]):
            streak+=1
        if(temps[i]>temps[i+1]):
            if(streak>longest_streak):
                longest_streak=streak
            streak=0
    print(longest_streak)


if __name__ == "__main__":
    main()