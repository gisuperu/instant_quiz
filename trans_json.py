#!/usr/bin//env Python3

import json
import csv


filename = "ns/range1"

importFile = "./org/" + filename + ".csv"
exportFile = "./json/" + filename +".json"

def reader(data): 
    # data : list型，追記されるだけ
    # importFileからデータを抽出する
    with open(importFile, "r") as imf:
        variety = "undefined"
        for dataline in imf:
            line = [str(s.strip()) for s in dataline.split(',')]
            if len(line)==0:
                variety = line[0]
            else:
                data.append(line.append(variety))

def writer(data):
    # すでにjsonファイルが生成済みの場合，複製(.sample)を作成する
    print("hoge")

    # 辞書型dataからjsonファイルをexportFileに出力する
    print("hoge")

def main():
    data = reader([])
    writer(data)
    print("finish")

if __name__=="__main__":
    main()