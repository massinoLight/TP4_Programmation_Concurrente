from multiprocessing import Process


def __calcul_square__(item=1):
    print(str(item) +'^2='+str(item**2) + ' ')


def __calcul_cube__(item=1):
    print(str(item)+'^3='+str(item ** 3) + ' ')



if __name__ == "__main__":
    liste = [2, 3,8,9,12]
    procs = []

    for i in liste:
        proc = Process(target=__calcul_square__, args=(i,))
        proc2 = Process(target=__calcul_cube__, args=(i,))
        procs.append(proc)
        procs.append(proc2)

    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()
