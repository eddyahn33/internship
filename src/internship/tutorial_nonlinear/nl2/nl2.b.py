def GC_twenty(r_seq):
    if len(r_seq) < 20:
        print("sequence length should be at least 20 nt")
        return None
    GC_window = r_seq[0:20].count("G") + r_seq[0:20].count("C")
    maxGC = GC_window
    minGC = GC_window
    for start in range(1, len(r_seq) - 19):
        if r_seq[start + 19] in "GC":
            GC_window += 1    
        
        if r_seq[start - 1] in "GC":
            GC_window -= 1
        
        maxGC, minGC = max(maxGC, GC_window), min(minGC, GC_window)
    
    print(maxGC / 20, minGC / 20)
    return maxGC / 20, minGC / 20

test = "GGGGGCCCCCGGGGGCCCCCGGGGGCCCCCAAAAAAAAAA"

GC_twenty(test)