    hablar sobre el uso del is que compara ubicaciones de memoria y no valores
    
    while seqs:
        r  = left_read(seq, seqs)
        if not r:
            break
        seq_over, i, i_ovr = r
        if seq_over:
            seq = seq_over[:-i_ovr] + seq
            seqs.pop(i)

            el if seq_over ya no es necesario porque con el if not r: break me aseguro que left read no devuelva un none