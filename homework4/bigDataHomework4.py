import json

#拿到所有文件的数据，以List形式返回
def getDocDataByList():
    tempDataStrList=[]
    for index,tempDocName in enumerate(docNameList):
        f = open(docNameList[index])
        tempDataStrList.append(f.read())
    return tempDataStrList

#拿到对象字典
def getDataDictBySet():
    tempStr = ''
    for item in dataStrList:
        tempStr += item+' '
    return set(tempStr[:-1].split(' '))

#输入关键字返回踪迹文件个数
def getRightDocsNum(keyword):
    count = 0
    for item in dataStrList:
        if(keyword in item.split(' ')):
            count += 1
    return count

#输入关键字返回其在指定文件中出现次数
#keyword,docIndex：0~3
def getNumInDoc(keyword,docIndex):
    return dataStrList[docIndex].count(keyword)

#返回指定文件数据：
def getDocDataNum(docIndex):
    return len(dataStrList[docIndex].split(' '))

def main():
    global docNameList
    global dataStrList
    docNameList = ['d1.txt', 'd2.txt', 'd3.txt', 'd4.txt']

    dataStrList = getDocDataByList()
    dataSet = getDataDictBySet()
    result = {}
    for keywordItem in list(dataSet):
        result[keywordItem] = {}
        result[keywordItem]['docNum'] = getRightDocsNum(keywordItem)
        result[keywordItem]['docList'] = {}
        for index,docNameItem in enumerate(docNameList):
            if(getNumInDoc(keywordItem, index)):
                result[keywordItem]['docList'][docNameItem] = [getNumInDoc(keywordItem, index), getDocDataNum(index)]
    # print(result)
    # with open("./result.json","w") as f:
    #     json.dump(json.dumps(result, indent=4, ensure_ascii=False),f)
    #     print("加载入文件完成...")
    print(json.dumps(result, indent=4, ensure_ascii=False))



if __name__ == '__main__':
    main()