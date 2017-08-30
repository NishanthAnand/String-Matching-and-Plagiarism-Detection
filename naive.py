def search(pat, txt, marked_sentences, index):
    M = len(pat)
    N = len(txt)

    # A loop to slide pat[] one by one
    for i in range(N):

        # For current index i, check for pattern match
        for j in range(M):
            if txt[i + j] != pat[j]:
                break
            elif j == M - 1:  # if pat[0...M-1] = txt[i, i+1, ...i+M-1]
                marked_sentences[index] = 1
                return (pat, marked_sentences, index)

    return (' ', marked_sentences, index)
