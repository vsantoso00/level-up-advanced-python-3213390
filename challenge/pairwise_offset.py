

def pairwise_offset(sequence, fillvalue='*', offset=0):
    """Pairwise offset generator."""
    pairwise = []
    sequence2 =  list(fillvalue * offset) + [i for i in sequence]
    sequence =  [i for i in sequence] +list(fillvalue*offset)


    for i in range(len(sequence)):
            pairwise.append((sequence[i], sequence2[i]))
    return pairwise

#print(pairwise_offset(['a','b','c'], offset=2))