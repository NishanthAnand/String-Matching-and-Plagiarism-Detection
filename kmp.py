def computeLPSArray(pattern, prefix_array):
    prefix_suffix_length = 0

    prefix_array[0] = 0
    index = 1


    while index < len(pattern):
        if pattern[index] == pattern[prefix_suffix_length]:
            prefix_suffix_length += 1
            prefix_array[index] = prefix_suffix_length
            index += 1
        else:
            if prefix_suffix_length != 0:
                prefix_suffix_length = prefix_array[prefix_suffix_length - 1]
            else:
                prefix_array[index] = 0
                index += 1


def KMPSearch(pattern, text, marked_sentences, index):
    prefix_array = [0] * len(pattern)
    pattern_index = 0  # index for pat[]
    pattern_length = len(pattern)
    text_length = len(text)

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pattern, prefix_array)

    text_index = 0  # index for txt[]
    while text_index < text_length:
        if pattern[pattern_index] == text[text_index]:
            text_index += 1
            pattern_index += 1

        if pattern_index == pattern_length:
            marked_sentences[index] = 1
            return (pattern, marked_sentences, index)
            #return "true"

        # mismatch after j matches
        elif text_index < text_length and pattern[pattern_index] != text[text_index]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if pattern_index != 0:
                pattern_index = prefix_array[pattern_index - 1]
            else:
                text_index += 1

    return (' ', marked_sentences, index)
    return "false"
