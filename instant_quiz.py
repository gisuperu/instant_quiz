#!/usr/bin//env Python3

import json
import random


questionFile = "./json/{}.json"
nsFilenames = ["ns/range1"]

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
        return True
    except:
        # 出題失敗
        return False

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
        return True
    except:
        # 出題失敗
        return False

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
        return True
    except:
        # 出題失敗
        return False

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
        else:
            print("--- 不正解… ---")
            print("({0}) {1}".format(**answer))
        return True
    except:
        # 出題失敗
        return False

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
                break
        return True
    except:
        # 出題失敗
        return False

def ns_quiz(data):
    type = data["type"]
    istake = False

    if type=="select":
        istake = ns_select(**data)
    elif type=="sort":
        istake = ns_sort(**data)
    elif type=="equal":
        istake = ns_equal(**data)
    elif type=="tof":
        istake = ns_tof(**data)
    elif type=="fill":
        istake = ns_fill(**data)
    
    return istake

def main():
    print("hello")

if __name__=="__main__":
    main()