import sys
import numpy as np
from prettytable import PrettyTable
import Lexical_analysis





def read_source_file(file) :
    global grammer
    f = open(file, "r",encoding="UTF-8")
    grammer = f.readlines()
    f.close()
    count = 0
    for line in grammer :
        str = ""
        list = []
        for i in line:
            if i == "<":
                str = ""
                continue
            if i == ">":
                list += [str.strip()]
                #if isterminal(str.strip()):
                    #print(str.strip())
            str += i
        grammer[count]=list
        count += 1

def is_terminal(str):
    #return Lexical_analysis.is_keyword(str) or Lexical_analysis.is_operator(str) or Lexical_analysis.is_separator(str)
    return str in Lexical_analysis.CATEGORY_DICT
def is_kong(str):
    return str == "空"

def getFirst():
    global first
    first = {}
    #初始化 and 若X是终结符，则FIRST(X) = {X}。
    for line in grammer:
        for i in line:
            if is_terminal(i) or is_kong(i):
                first[i] = [i]
            else:
                first[i] = []

    while(1):
        f=0
        for line in grammer:
            k = 1
            test = first[line[0]].copy()
            for i in line[1:]:
                k += 1
                if "空" not in first[i]:
                    first[line[0]] += first[i]
                    first[line[0]] = list(set(first[line[0]]))
                    break
                elif k == len(line):
                    first[line[0]] += first[i]
                    first[line[0]] = list(set(first[line[0]]))
                else :
                    t = first[i]
                    t.remove("空")
                    first[line[0]] += t
                    first[line[0]] = list(set(first[line[0]]))
            if len(test) != len(first[line[0]]):
                f = 1
        if not f:
           break

def getFollow():
    global follow
    follow = {}
    #初始化
    for line in grammer:
        for i in line:
            if not is_terminal(i):
                if i !="空":
                    follow[i] = []
    follow["开始"] +=["#"]

    while(1):
        f=0
        for line in grammer:
            for i in range(len(line)-1):
                if is_terminal(line[i+1]):
                    continue
                if line[i+1] == "空":
                    continue
                test = follow[line[i + 1]].copy()
                #判断line[i]是不是表达式的最后一个字符
                if len(line)-1 == i+1 :
                    follow[line[i + 1]] += follow[line[0]]
                    follow[line[i + 1]] = list(set(follow[line[i + 1]]))
                #循环line[i]之后的字符
                for j in range(len(line)-1-i-1):
                    if is_terminal(line[i+j+2]):
                        follow[line[i + 1]] += first[line[i + j + 2]]
                        break
                    elif "空" in first[line[j + i + 2]]:
                        if i + j + 2 == len(line) - 1:
                            follow[line[i + 1]] += follow[line[0]]
                            follow[line[i + 1]] += first[line[i + j + 2]]
                        else:
                            follow[line[i + 1]] += first[line[i + j + 2]]
                    else:
                        follow[line[i + 1]] += first[line[i + j + 2]]
                follow[line[i + 1]] = list(set(follow[line[i + 1]]))
                if "空" in follow[line[i + 1]]:
                    follow[line[i+1]].remove("空")
                if len(test) != len(follow[line[i + 1]]):
                    f = 1
        if not f:
            break

def getSelect():
    global select
    select = {}
    #初始化
    for line in grammer:
        select[grammer.index(line)] = []
    a = -1
    for line in grammer:
        a += 1
        b = 0
        for i in line[1:]:
            b +=1
            if "空" in first[i]:
                first[i].remove("空")
                select[a] += first[i]
                first[i]+=["空"]
            else:
                select[a] += first[i]
                break;
        if b == len(line)-1 and "空" in first[line[-1]]:
            select[a] += follow[line[0]]
            select[a] = list(set(select[a]))


def getLL_1Table():
    global terminal
    terminal = []
    global nterminal
    nterminal = []
    global LL_1Table
    for i in grammer:
        for j in i:
            if is_terminal(j):
                terminal += [j]
            else :
                nterminal += [j]
    terminal = list(set(terminal))
    terminal += ["空"]
    nterminal = list(set(nterminal))
    nterminal.remove("空")
    terminal += ("#")
    LL_1Table = -np.ones((len(nterminal),len(terminal)))
    k = int(0)
    for line in select:
        for i in select[line]:
            if LL_1Table[nterminal.index(grammer[k][0])][terminal.index(i)] == -1:
                LL_1Table[nterminal.index(grammer[k][0])][terminal.index(i)] = k
            else:
                print("error：文法错误")
                print(nterminal.index(grammer[k][0]) ,terminal.index(i), LL_1Table[nterminal.index(grammer[k][0])][terminal.index(i)],k)

        k += 1
    print_Table(LL_1Table)

def print_Table(a):
    tb = PrettyTable()
    row1 = terminal
    row1.insert(0," ")
    tb.field_names = row1
    k=0

    for i in a:
        t = i
        t1 = t.tolist()
        t1 = [nterminal[k]]+t1
        tb.add_row(t1)
        k +=1
    print(tb)

def print_all():
    global first,follow,select,result
    tb1 = PrettyTable()
    tb1.field_names=["字符","FIRST集"]
    for line in first:
        t =[str(line)]+[" ".join(first[line])]
        tb1.add_row(t)
    print(tb1)

    print("***********************************************************")
    tb2 = PrettyTable()
    tb2.field_names = ["非终结符","FOLLOW集"]
    for line in follow:
        t =[str(line)]+[" ".join(follow[line])]
        tb2.add_row(t)
    print(tb2)
    print("***********************************************************")
    tb3 = PrettyTable()
    tb3.field_names = ["产生式序号","SELECT集"]
    for line in select:
        t = [str(line)] + [" ".join(select[line])]
        tb3.add_row(t)
    print(tb3)
    print("****************************************************************************     LL(1) 分 析 表       **************************************************************************************")
    getLL_1Table()
    print()
    print("******************************************************************    LL(1) 分 析 过 程       *************************************************************************")
    print()
    return 0


def is_not_ch(ch):
    return ch not in ["OP","SEP"]

def analysis():

    global analysis_result,analysis_result2
    analysis_result,analysis_result2 = [],[]
    stack_1 = ["#","开始"]
    stack_2 = result
    print(stack_2)
    print(stack_1[0])

    count = 15

    while(count):

        if stack_2[0] =="#":
            str1 = "#"
        elif stack_2[0][1] in terminal:
            str1 = stack_2[0][1]
        else:
            if Lexical_analysis.is_operator(stack_2[0][1]):
                str1="OP"
            elif Lexical_analysis.is_separator(stack_2[0][1]):
                str1="SEP"
            else:
                str1=stack_2[0][0]


        if stack_1[-1]=="#" and "#" in stack_2[0]:
            print(stack_1)
            print(stack_2)
            print("EOF")
            break
        elif stack_1[-1] in nterminal:
            print(str1)
            a =str(int( LL_1Table[nterminal.index(stack_1[-1])][terminal.index(str1)-1]))
            print(stack_1)
            print(stack_2)
            print("根据产生式 " + a+" 代入")
            analysis_result += [a]
            print()
            a = LL_1Table[nterminal.index(stack_1[-1])][terminal.index(str1)-1]
            if grammer[int(a)][1] == "空":
                stack_1 = stack_1[0:-1]
            else:
                stack_1 = stack_1[0:-1]
                list_a = grammer[int(a)][:0:-1]
                stack_1 += list_a

        elif stack_1[-1] == str1:
            print(stack_1)
            print(stack_2)
            print("匹配")
            analysis_result2 += [stack_2[0]]
            print()
            stack_1 = stack_1[0:-1]
            stack_2.remove(stack_2[0])
        else :

            print("error:语法分析错误")
            print(str1)
            print(stack_1)
            print(stack_2)
            break


def main() :
    file_name = "grammer.txt"
    read_source_file(file_name)
    global result
    result = Lexical_analysis.main()
    getFirst()
    getFollow()
    getSelect()
    print_all()
    analysis()
    print()
    return analysis_result,analysis_result2
if __name__ == "__main__":
    main()