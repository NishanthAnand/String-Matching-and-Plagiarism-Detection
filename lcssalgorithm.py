def lcss(text, pattern,  marked_sentences, index):
    text_length = len(text)
    pattern_length = len(pattern)
    lcss_matrix = [[0]*(pattern_length+1) for y in range(text_length+1)]
    length_of_lcss = 0

    for i in range(1, text_length+1):
        for j in range(1, pattern_length+1):
            if text[i-1] == pattern[j-1]:
                lcss_matrix[i][j] = lcss_matrix[i-1][j-1] + 1
            else:
                lcss_matrix[i][j] = max(lcss_matrix[i-1][j], lcss_matrix[i][j-1])

            if lcss_matrix[i][j]>length_of_lcss :
                length_of_lcss = lcss_matrix[i][j]

    if length_of_lcss == pattern_length :
        marked_sentences[index] = 1
        return (pattern, marked_sentences, index)
    else:
        return (' ', marked_sentences, index)
