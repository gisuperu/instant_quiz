#!/usr/bin//env Python3

import json
import random


questionFile = "./json/{}.json"
nsFilenames = ["ns/range1"]
quizSize = 20

# ns問題
def ns_select(type, variety, question, choices, answer):
    try:
        # 出題
        # print("問題種別: {0}, ジャンル: {1}".format(type, variety))
        print("問題種別: {0}".format(type))
        print("Q: {0}".format(question))
        print("選択肢: ", end="")
        for i in range(len(choices)):
            print("({0}) {1}, ".format(i+1, choices[i]), end="")
        print("\n")
        # 解答
        while True:
            ans = input("answer(Integer): ").strip()
            if str.isdecimal(ans):
                break
        if ans==answer:
            print("--- 正解！ ---")
        else:
            print("--- 不正解… ---")
            print(answer)
            return 2
        return 1
    except:
        # 出題失敗
        return 0

def ns_sort(type, variety, question, choices, answer):
    try:
        # 出題
        # print("問題種別: {0}, ジャンル: {1}".format(type, variety))
        print("問題種別: {0}".format(type))
        print("Q: {0}".format(question))
        print("選択肢: ", end="")
        for i in range(len(choices)):
            print("({0}) {1}, ".format(i+1, choices[i]), end="")
        print("\n")
        # 解答
        ans = input("answer(String): ").strip()
        if ans==answer:
            print("--- 正解！ ---")
        else:
            print("--- 不正解… ---")
            print(answer)
            return 2
        return 1
    except:
        # 出題失敗
        return 0

def ns_equal(type, variety, question, answer):
    try:
        # 出題
        # print("問題種別: {0}, ジャンル: {1}".format(type, variety))
        print("問題種別: {0}".format(type))
        print("Q: {0}, {1}".format(**question))
        # 解答
        ans = input("answer(String): ").strip()
        if ans==answer:
            print("--- 正解！ ---")
        else:
            print("--- 不正解… ---")
            print(answer)
            return 2
        return 1
    except:
        # 出題失敗
        return 0

def ns_tof(type, variety, question, choices, answer):
    try:
        # 出題
        # print("問題種別: {0}, ジャンル: {1}".format(type, variety))
        print("問題種別: {0}".format(type))
        print("Q: {0}".format(question))
        print("選択肢: ", end="")
        for i in range(len(choices)):
            print("({0}) {1}, ".format(i+1, choices[i]), end="")
        print("\n")
        # 解答
        while True:
            ans = input("answer(Integer): ").strip()
            if str.isdecimal(ans):
                break
        if ans==answer[0]:
            ans = input("answer(String): ")
            if ans==answer[1]:
                print("--- 正解！ ---")
            else:
                print("--- 不正解… ---")
                print("({0}) {1}".format(**answer))
                return 2
        else:
            print("--- 不正解… ---")
            print("({0}) {1}".format(**answer))
            return 2
        return 1
    except:
        # 出題失敗
        return 0

def ns_fill(type, variety, question, answer):
    try:
        # 出題
        # print("問題種別: {0}, ジャンル: {1}".format(type, variety))
        print("問題種別: {0}".format(type))
        print("Q: {0}, {1}".format(**question))
        # 解答
        for i in range(len(answer)):
            ans = input("{}. answer(String): ".format(i)).strip()
            if ans==answer[i]:
                print("--- 正解！ ---")
            else:
                print("--- 不正解… ---")
                print("答え: ", end="")
                for aa in answer:
                    print("{1}, ".format(aa), end="")
                print()
                return 2
        return 1
    except:
        # 出題失敗
        return 0

def ns_quiz(data):
    type = data["type"]
    result = 0

    if type=="select":
        result = ns_select(**data)
    elif type=="sort":
        result = ns_sort(**data)
    elif type=="equal":
        result = ns_equal(**data)
    elif type=="tof":
        result = ns_tof(**data)
    elif type=="fill":
        result = ns_fill(**data)
    
    return result

def main():
    print("選択肢: ", end="")
    for i in range(len(nsFilenames)):
        print("({0}) {1}, ".format(i+1, nsFilenames[i]), end="")
    print("\n")
    selectFile = -10000
    while int(selectFile) >= 0 and int(selectFile) < len(nsFilenames):
        selectFile = input("select File number: ")
    
    with open(questionFile.format(nsFilenames[selectFile]), "r", encoding="utf-8") as qf:
        data_dic = json.load(qf)
        
        while True:
            done_quiz = set([])
            numAns = 0
            i = 0
            while(i < quizSize):
                rnd = random.randrange(len(data_dic))
                if rnd not in done_quiz:
                    isb = ns_quiz(data_dic[rnd])
                    if isb==1 :
                        numAns += 1
                        i += 1
                    elif isb==2 :
                        i += 1
                elif len(done_quiz) > len(data_dic):
                    break
                done_quiz.add(rnd)
            print("result: {0}/{1}".format(numAns, quizSize))
            while True:
                sel = input("0:good bye. else:continue.  : ").strip()
                if sel=="0":
                    break

if __name__=="__main__":
    main()