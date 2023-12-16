def fibonnacci_recursive(a):
    if a <=1:
        return 1
    return fibonnacci_recursive(a-1) + fibonnacci_recursive(a-2)




def main():
    for a in range (20):
        print(fibonnacci_recursive(a))


if __name__ == "__main__":
    main()