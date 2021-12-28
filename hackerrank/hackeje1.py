##https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(raw_input())
    count = 0
    lista_nueva = []
    while count >= 0 and count < n:
        number_to_add = count **2
        print(number_to_add)
        count += 1   