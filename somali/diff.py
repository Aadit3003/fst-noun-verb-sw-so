import sys

def read_file(filename):
    with open(filename) as f:
        lines = [line.rstrip() for line in f]

    return lines

def list_to_dic(words):
    dic = {}
    for w in words:
        if w in dic:
            dic[w] += 1
        else:
            dic[w] = 1

    return dic

def get_wrongs(corrects, wrongs):
    correct_dic = list_to_dic(corrects)

    # print(correct_dic)

    mistakes = []

    for wrong in wrongs:
        if wrong not in correct_dic:
            mistakes.append(wrong)
        else:
            correct_dic.pop(wrong)

    correct_versions = list(correct_dic.keys())
    mistakes = mistakes

    print(len(mistakes), " mistakes!!")
    return mistakes, correct_versions

if __name__ == '__main__':
    correct_file = sys.argv[1]
    wrong_file = sys.argv[2]

    corrects = read_file(correct_file)
    # print(corrects)
    # print(len(corrects))
    print("_____________")

    wrongs = read_file(wrong_file)
    # print(wrongs)
    # print(len(wrongs))

    mistakes, corrections = get_wrongs(corrects, wrongs)
    mistakes.sort()
    corrections.sort()
    print("MISTAKES")
    print(mistakes)
    print("_________________")
    print("CORRECTIONS")
    print(corrections)