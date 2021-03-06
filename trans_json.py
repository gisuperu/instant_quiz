#!/usr/bin//env Python3

import json
import csv


filename = "ns/range2"

importFile = "./org/" + filename + ".csv"
exportFile = "./json/" + filename +".json"

def reader(data): 
    # data : list型，追記されるだけ
    # importFileからデータを抽出する
    with open(importFile, "r", encoding="utf-8") as imf:
        variety = "undefined"
        reader = csv.reader(imf)
        for dataline in reader:
            line = [str(s.strip()) for s in dataline]
            # line = dataline
            if len(line)==1:
                variety = line[0]
            else:
                line.append(variety)
                data.append(line)
    return data

def changer(deta):
    json_data = []

    # ns/ のフォーマット
    for line in deta:
        try:
            if line[1]=="select":
                json_data.append({
                    "idx" : int(line[0]),
                    "type" : line[1],
                    "variety" : line.pop(),
                    "question" : line[2],
                    "choices" : line[4:4+int(line[3])],
                    "answer" : int(line[-1])
                })
            elif line[1]=="sort":
                json_data.append({
                    "idx" : int(line[0]),
                    "type" : line[1],
                    "variety" : line.pop(),
                    "question" : line[2],
                    "choices" : line[4:4+int(line[3])],
                    "answer" : line[-1]
                })
            elif line[1]=="equal":
                json_data.append({
                    "idx" : int(line[0]),
                    "type" : line[1],
                    "variety" : line.pop(),
                    "question" : [line[2], line[3]],
                    "answer" : line[5:5+int(line[4])]
                })
            elif line[1]=="tof":
                json_data.append({
                    "idx" : int(line[0]),
                    "type" : line[1],
                    "variety" : line.pop(),
                    "question" : line[2],
                    "choices" : line[4:4+int(line[3])],
                    "answer" : [int(line[-2]), line[-1]]
                })
            elif line[1]=="fill":
                json_data.append({
                    "idx" : int(line[0]),
                    "type" : line[1],
                    "variety" : line.pop(),
                    "question" : line[2],
                    "answer" : line[4:4+int(line[3])]
                })
        except ValueError:
            import traceback
            traceback.print_exc()
            print(line[0], " is error")
    return json_data

def writer(data):
    try:
        # すでにjsonファイルが生成済みの場合，複製(.sample)を作成する
        with open(exportFile, "r", encoding="utf-8") as exf:
            with open(exportFile+".sample", "w", encoding="utf-8") as exfsample:
                for line in exf:
                    exfsample.write(line)
    except FileNotFoundError:
        print("new create a json file!")

    # 辞書型dataからjsonファイルをexportFileに出力する
    with open(exportFile, "w", encoding="utf-8") as exf:
        json.dump(data, exf, ensure_ascii=False, indent=2)

def main():
    data = reader([])
    # print(data)
    json_data = changer(data)
    # print(json_data)
    writer(json_data)
    print("finish")

if __name__=="__main__":
    main()