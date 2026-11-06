def GC_twenty(r_seq):
    if len(r_seq) < 20:
        print("sequence length should be at least 20 nt")
        return None
    maxGC = 0
    minGC = 20

    for start in range(0, len(r_seq) - 19, 20):
        GC_window = r_seq[start:start+20].count("G") + r_seq[start:start+20].count("C")
        maxGC, minGC = max(maxGC, GC_window), min(minGC, GC_window)
    
    print(maxGC / 20, minGC / 20)
    return maxGC / 20, minGC / 20

test = "GGGGGCCCCCGGGGGCCCCCGGGGGCCCCCAAAAAAAAAAAAAAAAAAAA"

GC_twenty(test)