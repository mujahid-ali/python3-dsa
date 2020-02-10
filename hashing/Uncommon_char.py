
def print_uncommon(str1, str2):
    MAX_CHAR = 26
    present = [0] * MAX_CHAR
    for i in range(0,MAX_CHAR):
        present[i] = 0
    for i in range(0,len(str1)):
        present[ord(str1[i]) - ord('a')] = 1

    for i in range(0,len(str2)):
        if(present[ord(str2[i]) - ord('a')] == 1 or
            present[ord(str2[i]) - ord('a')] == -1):
            present[ord(str2[i]) - ord('a')] = -1
        else:
            present[ord(str2[i]) - ord('a')] = 2

    for i in range(0, MAX_CHAR):
        if(present[i] == 1 or present[i] == 2):
            print(chr(i + ord('a')), end = "")
            #print(chr(i + ord('a')), end = " ")


def main():
    t = int(input())
    while t > 0:
        t = t - 1
        str1 = input()
        str2 = input()

        print_uncommon(str1,str2)
        print()

if __name__ == '__main__':
    main()
