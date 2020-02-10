from collections import Counter

def check_if_arr_equal(arr1, arr2, n):
    #hm = {}
    cnt = Counter()
    cnt2 = Counter()
    for i in arr1:
        cnt[i] +=1
    #print(cnt)
    for i in arr2:
        cnt2[i] +=1
    #print(cnt2)
    if cnt == cnt2:
        print("1")
    else:
        print("0")

def main():
    t = int(input())
    while t > 0:
        t = t - 1
        n = int(input())
        arr1 = [int(x) for x in input().split()]
        arr2 = [int(x) for x in input().split()]
        check_if_arr_equal(arr1, arr2, n)
if __name__ == '__main__':
    main()
