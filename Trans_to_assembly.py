import sys
import Semantic_analysis

def trans():
    global four,result ,AX, BX,CX
    result = []
    t = []
    data = [-1]*100

    rule = {
        "j==":["判断","JE"],
        "j>":["判断","JG"],
        "j<=":["判断","JNG"],
        "j<":["判断","JL"],
        "j>=":["判断","JNL"],
        "%":["运算",""],
        "=":["赋值","MOV"],
        "+":["运算","ADD"],
        "-":["运算","SUB"],
        "*":["运算","IMUL"],
        "/":["运算",""],
        "j":["转移","JMP"],
    }
    #print("error : 翻译错误")

    n = 0
    for line in four:
        if rule[line[0]][0] == "判断":
            t += [n+1]
        elif rule[line[0]][0] == "转移":
            t +=[n+1]
            t += [line[3]]
        n = n+1
    t = list(set(t))
    t.sort()
    four_in ={}
    m = 1
    for i in t:
        four_in[i] = "CODE"+str(m)
        m+=1
    print(four_in)

    tab =  "        "
    result += [("ASSUME CS:CODE,DS:DATA")]
    result += [("DATA SEGMENT")]
    result += [(tab+"DW 100 DUP(0)")]
    result += [("DATA ENDS")]
    result += [("CODE SEGMENT")]
    result += [("START:")]

    for i in range(len(four)):
        if i in four_in:
            result +=[four_in[i]+":"]
        if rule[four[i][0]][0] == "判断":
            result+=[tab+"MOV AX,DS:["+str(2*data.index(four[i][1]))+"]"]
            result+=[tab+"MOV BX,"+str(four[i][2])]
            result+=[tab+"CMP AX,BX"]
            result+=[tab+""+rule[four[i][0]][1]+" "+four_in[four[i][3]]]
            result+=[""]
        elif rule[four[i][0]][0] == "赋值":
            if isinstance(four[i][1],int) or isinstance(four[i][1],float):
                data[data.index(-1)] = four[i][3]
                result += [tab+"MOV AX,"+ str(four[i][1])]
                result += [tab+"MOV DS:["+str(2*data.index(four[i][3]))+"],AX"]
            else:
                data[data.index(-1)] = four[i][3]
                result += [tab+"MOV AX,DS:[" + str(2*data.index(four[i][1]))+"]"]
                result += [tab+"MOV DS:[" + str(2 * data.index(four[i][3])) + "],AX"]
        elif rule[four[i][0]][0] == "运算":
            if isinstance(four[i][1],int) or isinstance(four[i][1],float):
                result += [tab+"MOV AX,"+str(four[i][1])]
            else:
                result += [tab+"MOV AX,DS:[" + str(2*data.index(four[i][1]))+"]"]
            if isinstance(four[i][2],int) or isinstance(four[i][2],float):
                result += [tab+"MOV BX,"+str(four[i][2])]
            else:
                result += [tab+"MOV BX,DS:[" + str(2*data.index(four[i][2]))+"]"]
            if four[i][0] == "+" or four[i][0] == "-":
                result += [tab+rule[four[i][0]][1]+" AX,BX"]
            elif four[i][0] == "*":
                result += [tab+"IMUL BX"]
            elif four[i][0] == "/":
                result += [tab+"IDIV BX"]
            else:
                result +=["----运算符未定义---"]
            data[data.index(-1)] = four[i][3]
            result += [tab+"MOV AX,DS:["+str(2*data.index(four[i][3]))+"]"]

        elif rule[four[i][0]][0] == "转移":
            result +=[tab+"JMP "+str(four_in[four[i][3]])]
            result +=[""]
    result += [""]
    result += ["CODE"+str(m-1)+":"]
    result += [tab+"MOV AX,4c00"]
    result += [tab+"INT 21"]
    result += ["CODE ENDS"]
    result += ["END"]
    for line in result:
        print(line)

def main():
    global four
    four = Semantic_analysis.main()
    trans()

if __name__ == "__main__":
    main()
