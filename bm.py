import time


# Generate the Bad Character Skip List
def generateBadCharShift(term):
    skipList = {}
    for i in range(0, len(term) - 1):
        skipList[term[i]] = len(term) - i - 1
    return skipList


# Generate the Good Suffix Skip List
def findSuffixPosition(badchar, suffix, full_term):
    for offset in range(1, len(full_term) + 1)[::-1]:
        flag = True
        for suffix_index in range(0, len(suffix)):
            term_index = offset - len(suffix) - 1 + suffix_index
            if term_index < 0 or suffix[suffix_index] == full_term[term_index]:
                pass
            else:
                flag = False
        term_index = offset - len(suffix) - 1
        if flag and (term_index <= 0 or full_term[term_index - 1] != badchar):
            return len(full_term) - offset + 1


def generateSuffixShift(key):
    skipList = {}
    buffer = ""
    for i in range(0, len(key)):
        skipList[len(buffer)] = findSuffixPosition(key[len(key) - 1 - i], buffer, key)
        buffer = key[len(key) - 1 - i] + buffer
    return skipList


# Actual Search Algorithm
def BMSearch(haystack, needle, marked_sentences, index):
    before = time.time()
    # goodSuffix = generateSuffixShift(needle)
    # print "generateSuffixShift Algorithm:"+str(time.time()-before)
    before = time.time()
    badChar = generateBadCharShift(needle)
    # print "generateBadCharShift Algorithm:"+str(time.time()-before)

    i = 0
    while i < len(haystack) - len(needle) + 1:
        j = len(needle)
        while j > 0 and needle[j - 1] == haystack[i + j - 1]:
            j -= 1
        if j > 0:
            badCharShift = badChar.get(haystack[i + j - 1], len(needle))
            # goodSuffixShift = goodSuffix[len(needle)-j]
            # if badCharShift > goodSuffixShift:
            i += badCharShift
            # else:
            #   i += goodSuffixShift
        else:
            #print "Plagarized from file : " + filename
            #print "Plagarized sentence : " + needle + "\n\n"
            #s1[counter] = 1
            marked_sentences[index] = 1
            return (needle, marked_sentences, index)
    return (' ', marked_sentences, index)


    #if _name_ == "_main_":

#pat = "They have evidently come a long way, for they are tired, exhausted, and travel-stained."
#txt = """
        #It is built on a sunny plain, through which flow two rivers,--the Choaspes and the Ulai; he sees them both sparkling in the sunshine, as they wind through the green plain, sometimes flowing quite close to each other, at one time so near that only two and a half miles lie between them, then wandering farther away only to return again, as if drawn together by some subtle attraction.
#But the great Babylonian empire did not last long. Cyrus the Persian took Babylon, Belshazzar was slain, the great Assyrian power passed away, and the second great world-empire, the Persian empire, was built upon its ruins.
#He felt he could trust him fully, and he was not disappointed in his confidence, for the great Rab-shakeh served a higher Master than the King of Persia, he was a faithful servant of the God of Heaven.
#What do we know of Nehemiah? Can we say from our heart, 'The Lord is my Comforter?' I take Him my every sorrow, I tell Him my every trouble. He understands it, and He understands me, and He comforts me as no other can. The Lord is indeed my Comforter.
#Eight thousand Jews had been ready to leave comfort, luxury, and affluence behind, that they might go to the desolate city, and endeavour to stir up its people to energy and life.
#One of the 8,000 who went with Ezra was Nehemiah's brother, Hanani.
# They have evidently come a long way, for they are tired, exhausted, and travel-stained.
# Where can the caravan have come from? Nehemiah finds to his astonishment that it has come from Jerusalem, the city of cities, as he had been taught to believe it, and, to his still greater surprise, he finds amongst the travellers his long-lost brother Hanani.
# What is that plant standing in a conspicuous place in the conservatory? It is a beautiful azalea, covered with hundreds of pure white blossoms. But there is so much else to see in that conservatory that we scarcely notice it as we pass by. Nor are we at all surprised to see it there; it is just the very place in which we should look for such a plant.
# So it ever is. The plants of God's grace often thrive in very unlikely places. There was a holy Joseph in the court of Pharaoh, a faithful Obadiah in the house of wicked Jezebel, a righteous Daniel in Babylon, and saints even in Caesar's household.
# He does not speak, or see, or move, or feel. He is rubbed and warmed, but no sign of life can be perceived. Can we therefore conclude that the man is dead? Nay, we will put him to the test. Bring a feather, hold it before his mouth, watch it carefully, does it move?
# He had determined to speak to the great Persian monarch--to bring before him the desolate condition of Jerusalem, and to ask for leave of absence from the court at Shushan, in order that he might go to Jerusalem, and do all in his power to restore it to something of its former grandeur.
#     """
#     block = "This is a simple example"
#     print BMSearch(txt, pat)
#
#     # print "This is an example search on the string \"", block, "\"."
#     # print "ple  :", BMSearch(block, "ple ")
#     # print "example :", BMSearch(block, "example")
#  #print "simple :", BMSearch(block, "simple")
# print " imple :", BMSearch(block, " imple")