def counter(limit):
    result = 0
    scores = list()

    # build all possible single scores
    for i in range(1, 21):
        scores.append(i)
        scores.append(i * 2)
        scores.append(i * 3)
    scores.append(25)
    scores.append(50)

    # make all possible doubles
    doubles = list()
    for i in range(1, 21):
        doubles.append(i * 2)
    doubles.append(25 * 2)

    # count all miss, miss, double
    for third in doubles:
        if third <= limit:
            result += 1

    # count all miss, hit, double
    for i in range(len(scores)):
        for third in doubles:
            if scores[i] + third <= limit:
                result += 1

    # count all hit, hit, double
    for i in range(len(scores)):
        for j in range(i, len(scores)):
            for third in doubles:
                if scores[i] + scores[j] + third <= limit:
                    result += 1

    return result
