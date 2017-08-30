import glob
import lcssalgorithm as lcss
import kmp as kmp
import naive as naive
import bm as bm
import matplotlib.pyplot as plt
import numpy as np
import time
import os

thresh_hold = 25
input = open('input.txt', "rb")
inputsize = os.path.getsize("input.txt")
inputsize = os.stat('input.txt').st_size
target_folder = 'target'
total_time_array = []
size_array = []


def initialze_variables():
    #input_file_splits = input.read().split(".")
    input_file_splits = filter(None, input.read().split("."))
    all_target_files = glob.glob(target_folder+"/*.txt")

    #lcss
    check_for_all_file(all_target_files, input_file_splits,1)


    #naive
    check_for_all_file(all_target_files, input_file_splits,2)


    #kmp
    check_for_all_file(all_target_files, input_file_splits,3)


    #bm
    check_for_all_file(all_target_files, input_file_splits,4)
    #x = np.arange(10)
    print "time array"
    print total_time_array
    print size_array


def check_for_all_file(all_target_files,input_file_splits, algorithm):
    marked_sentences = []

    if algorithm == 1:
        print "KMP Search"
    elif algorithm == 4:
        print "LCSS Search"
    elif algorithm == 2:
        print "Naive Search"
    elif algorithm == 3:
        print "BM Search"

    for i in range(len(input_file_splits)):
        marked_sentences.append(0)
    before = time.time()
    for eachfile in all_target_files:
        marked_sentences = check_for_all_sentences(input_file_splits, eachfile, marked_sentences, algorithm)

    total_sentences_marked = 0

    for sentence in marked_sentences:
        total_sentences_marked = total_sentences_marked + sentence

    after = time.time()
    percentage_plagiraized = float(total_sentences_marked) * 100 / len(marked_sentences)
    print str(percentage_plagiraized) + " % Plagarized"
    print "Plagiarism threshhold is set to " + str(thresh_hold) + "%"
    print "Final report: "
    if(percentage_plagiraized > thresh_hold):
        print "File Plagiarized"
    else:
        print "File not plagiarised"

    timetaken = after-before
    total_time_array.append(float(timetaken))
    size_array.append(int(os.stat(eachfile).st_size))



    print "timetaken: "+str(timetaken)
    print "-----------------------------------------------------"


def check_for_all_sentences(input_file_splits, target_file, marked_sentences, algorithm):
    index = 0;
    splits_plagiarized = []
    target_file_content = open(target_file, "rb").read()

    for asplit in input_file_splits:
        if algorithm == 1:
            #print "KMP Search"
            pattern, marked_sentences, index = kmp.KMPSearch(asplit, target_file_content, marked_sentences, index)
        elif algorithm == 4:
            #print "LCSS Search"
            pattern, marked_sentences, index = lcss.lcss(target_file_content,asplit,  marked_sentences, index)
        elif algorithm == 2:
            #print "Naive Search"
            pattern, marked_sentences, index = naive.search(asplit,target_file_content,  marked_sentences, index)
        elif algorithm == 3:
            #print "BM Search"
            pattern, marked_sentences, index = bm.BMSearch(target_file_content,asplit,  marked_sentences, index)

        index += 1;
        if (str(pattern) != ' '):
            splits_plagiarized.append(pattern)
    print "\n\n\nPlagarized from file : "+ target_file + " Size :" + str(os.stat(target_file).st_size) +"\n"
    print splits_plagiarized
    return marked_sentences

initialze_variables()

