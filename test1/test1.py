def main():
    print("Print your n and m with space between them: ")
    n, m = map(int, input().split())
    i = 1
    while True:
        print(i, end='')
        i = 1 + (i + m - 2) % n
        if i == 1:
            break
    print()

if __name__ == '__main__':
    main()
    input('Press ENTER to exit')
