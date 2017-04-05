


def main():
    n = int(input())
    productivity = list()
    managers = list()

    for i in range(n):
        p_val, manager_i = [int(x) for x in input().split()]
        productivity.append(p_val)
        managers.append(manager_i)


    subordinate = dict()

    for sub in range(n):
        manager = managers[sub]
        print(sub)
        subordinate[manager] = subordinate.get(manager,[]).append(sub)
    print(subordinate)    









if __name__ == '__main__':
    main()
