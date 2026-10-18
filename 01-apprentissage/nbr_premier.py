
def est_premier(nombre):
    if nombre < 2:
        return False
    else:
        for i in range(2, (nombre //2 ) +1):
            if nombre % i == 0:
                return False
    return True

