def KFOLD(DATA, NUM_CLASSES, KFOLD):
    CLS_TMP = list()
    for i in range(NUM_CLASSES):
        clssp = []
        for j in DATA:
            if int(j[-1]) == i:
                clssp.append(j)
        clssp = np.array(clssp)
        CLS_TMP.append(clssp)

    def KFOLD_SEPARATION(sample):
        getsam = sample
        kfoldset = []
        for i in range(KFOLD):
            putnum = len(getsam) // (KFOLD - i)
            wtput = getsam[:putnum]
            kfoldset.append(wtput)
            getsam = getsam[putnum:]

        return kfoldset

    SEPARATED_SET = []
    for i in CLS_TMP:
        SEPARATED_SET.append(KFOLD_SEPARATION(i))

    FINAL_SET = []
    for i in range(KFOLD):
        FINAL_SET.append(np.vstack([SEPARATED_SET[j][i] for j in range(NUM_CLASSES)]))

    return FINAL_SET