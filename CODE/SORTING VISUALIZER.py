# sample input given below: 
# 4 25 12 22 11 78 91 3 45 56 19 88 72 34 67 5 99 41 28 60 14 83 7 52 30 95 1 48 76 20 69 9 37 58 81 16 97 24 43 62 10 85 32 74 6 93 27 50 18 71

import os
import time
import winsound

speedset=0
#funtion for creating a visual list
def visual_list(l):
    visual = []
    for k in l:
        count = 1
        for m in l:
            if k > m:
                count += 1
        visual.append(count)
    return visual

#funtion for creating visualization pattern
def pattern(visual, l, n):

    os.system('cls')
    max_height = max(visual)
    print("\nSORTING ALGORITHM VISUALIZATION\n")
    for level in range(max_height, 0, -1):
        for bar in visual:
            if bar >= level:
                print(" 🟩 ", end="")
            else:
                print("    ", end="")
        print()

    for num in l:
        print(f" {num:02d}", end=" ")

    print()
    time.sleep(speedset)
    winsound.Beep(100,100)

#funtion for updating the screen
def printing(l):
    visual = visual_list(l)
    pattern(visual, l, len(l))


def partition(arr, low, high):

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            printing(arr)
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    printing(arr)
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def selectionsort(l):
    for i in range(0,n):
        small=i
        for j in range(i+1,n):
            if l[j]<l[small]:
                small=j
                
        temp=l[i]
        l[i]=l[small]
        l[small]=temp
        printing(l)

def bubblesort(arr):
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
        printing(arr)

os.system('cls')

#USER MENU
print("\nSORTING ALGORITHM VISUALIZATION\n")
while True:
    l=list(map(int, input("\nENTER NUMBERS SEPARATED BY SPACES : ").split()))
    n=len(l)
    print("\nPress '1' for SELECTION SORT")
    print("Press '2' for BUBBLE SORT")
    print("Press '3' for QUICK SORT")
    print("Press '4' for EXIT")
    choice=int(input("\nENTER YOUR CHOICE : "))
    
    print("\nCHOICE VISUALIZATION SPEED : \nPress '1' for FAST\nPress '2' for MEDIUM\nPress '3' for SLOW\n")
    speed=int(input("ENTER YOUR SPEED CHOICE : "))
    if speed==1:
        speedset=0.10
    elif speed==2:
        speedset=0.15
    elif speed==3:
        speedset=0.25

    if choice==4:
        break
    else:
        printing(l)
        if choice==1:
            selectionsort(l)
        elif choice==2:
            bubblesort(l)
        elif choice==3:
            quicksort(l, 0, len(l) - 1)
        else:
            print("INVALID INPUT")
            continue
        
    print("\nSORTED LIST: \n", end="")
    print(l)
