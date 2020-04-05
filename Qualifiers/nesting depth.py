if __name__ == '__main__':
    from sys import stdin, stdout

    results = []

    for i in range(int(input())):

        new_sstr = list(input())
        nd = 0
        MY_own_new = []
        for x in new_sstr:
            for j in range(int(x)):
                MY_own_new.append('(')
            MY_own_new.append(x)
            for j in range(int(x)):
                MY_own_new.append(')')

        str_MY_own_new = ''.join(MY_own_new)

        while ')(' in str_MY_own_new:
            list_sMY_own_new = str_MY_own_new.split(')(')
            str_MY_own_new = ''.join(list_sMY_own_new)

        results.append(str_MY_own_new)

    for index in range(len(results)):
        print('Case #{}: {}'.format(index + 1, results[index]))