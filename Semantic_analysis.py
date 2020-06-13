import Parser

global Parser_r1, Parser_r2,temp,four

def goon(a):
    global Parser_r1, Parser_r2, temp
    print()
    print(Parser_r1)
    print(Parser_r2)
    print(temp)
    if a ==1:
        b = Parser_r1[0]
        str1 = "fun_"+str(b)+"()"
        return eval(str1)
    else:
        temp +=[ Parser_r2[0]]
        t =[ Parser_r2[0]]
        Parser_r2 = Parser_r2[1:]
        return  t

def fun_0():
    global Parser_r1, Parser_r2,temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(1)
    goon(2)
    goon(2)
    goon(2)
    goon(1)
    goon(2)
    temp = temp[:-7]
    temp += []
    return 0

def fun_1():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(1)
    goon(2)
    temp = temp[:-3]
    temp += [("语句列表",-1,-1)]
    return 0

def fun_2():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(2)
    return 0

def fun_3():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(2)
    return 0

def fun_4():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(2)
    return 0

def fun_5():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(1)
    temp = temp[:-2]
    temp +=[("语句列表",-1,-1)]
    return 0

def fun_6():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    temp += [("语句列表", -1, -1)]
    return 0

def fun_7():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(2)
    temp = temp[:-2]
    temp += [("语句",-1,-1)]
    return 0

def fun_8():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(2)
    temp = temp[:-2]
    temp += [("语句",-1,-1)]
    return 0

def fun_9():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    temp = temp[:-1]
    temp +=[("语句",-1,-1)]
    return 0

def fun_10():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    temp = temp[:-1]
    temp += [("语句", -1, -1)]
    return 0

def fun_11():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    temp = temp[:-1]
    temp += [("语句", -1, -1)]
    return 0

def fun_12():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    temp = temp[:-1]
    temp += [("语句", -1, -1)]
    return 0

def fun_13():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    temp = temp[:-1]
    temp += [("语句", -1, -1)]
    return 0

def fun_14():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(1)
    goon(1)
    temp = temp[:-3]
    temp += [("声明语句",-1,-1)]
    return 0

def fun_15():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    temp = temp[:-1]
    temp += [("声明语句2",-1,-1)]
    return 0

def fun_16():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(1)
    temp = temp[:-2]
    temp += [("声明语句3",-1,-1)]
    return 0

def fun_17():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    temp += [("声明语句3", -1, -1)]
    return 0

def fun_18():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(1)
    temp [-2] = temp[-1]
    temp = temp[:-1]
    return 0

def fun_19():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    return 0

def fun_20():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    temp += [("赋值语句1", -1, -1)]
    return 0

def fun_21():
    global Parser_r1, Parser_r2, temp,four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(1)
    print("---------------", temp)
    if temp[-2][1] == "=":
        print(("=",temp[-1][1],"_",temp[-3][1]))
        four +=[("=",temp[-1][1],"_",temp[-3][1])]
    else:
        print(("=", temp[-1][1], "_", temp[-2][1]))
        four += [("=", temp[-1][1], "_", temp[-2][1])]
   # print((temp[-2][1],temp[-1][1],"_",temp[-3][1]))
   # four += [(temp[-2][1],temp[-1][1],"_",temp[-3][1])]
    temp = temp[:-2]
    temp += [("赋值语句2", -1, -1)]
    return 0

def fun_22():
    global Parser_r1, Parser_r2, temp,four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    print(("+",temp[-2][1],1,temp[-2][1]))
    four += [("+",temp[-2][1],1,temp[-2][1])]
    return 0

def fun_23():
    global Parser_r1, Parser_r2, temp,four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    print(("+",temp[-2][1],1,temp[-2][1]))
    four += [("-",temp[-2][1],1,temp[-2][1])]
    return 0

def fun_24():
    global Parser_r1, Parser_r2,temp,four,ntemp
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(1)
    print(("=", 0, "_", "t" + str(ntemp)))
    four += [("=", 0, "_", "t" + str(ntemp))]
    four += [("j","_","_",len(four)+2)]
    print(("=",1,"_","t"+str(ntemp)))
    four +=[("=",1,"_","t"+str(ntemp))]
    temp[-2] =(temp[-1][0],"t"+str(ntemp),-1)
    temp = temp[:-1]
    ntemp +=1
    print(Parser_r1)
    print(Parser_r2)
    print(temp)

    return 0

def fun_25():
    global Parser_r1, Parser_r2, temp,four
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(1)
    print("--------------------------------")
    print(temp)
    if temp[-2][1] != "=" and temp[-3][1] != "=":
        print(("j" + str(temp[-2][1]), temp[-3][1], temp[-1][1], len(four) + 3))
        four += [("j" + str(temp[-2][1]), temp[-3][1], temp[-1][1], len(four) + 3)]
    elif temp[-2][1] != "=" :
        if temp[-3][1] != "=":
            print((str(temp[-3][1]), temp[-2][1], temp[-1][1], len(four) + 3))
            four += [(str(temp[-3][1]), temp[-2][1], temp[-1][1], len(four) + 3)]

    print(temp)
    temp[-2] = temp[-1]
    temp = temp[:-1]
    return 0

def fun_26():
    global Parser_r1, Parser_r2, temp ,ntemp ,four
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(1)
    print((temp[-2][1],temp[-3][1],temp[-1][1],"t"+str(ntemp)))
    four +=[(temp[-2][1],temp[-3][1],temp[-1][1],"t"+str(ntemp))]
    temp = temp[:-2]
    temp += [(temp[-1][0], "t"+str(ntemp), temp[-1][2])]
    ntemp +=1
    return 0

def fun_27():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    return 0

def fun_28():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    return  0

def fun_29():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    return 0

def fun_30():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(1)
    temp[-2] = temp[-1]
    temp = temp[:-1]
    return 0

def fun_31():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    temp += [temp[-1]]
    return 0

def fun_32():
    global Parser_r1, Parser_r2, temp,four,ntemp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(1)
    print((temp[-2][1],temp[-3][1],temp[-1][1],"t"+str(ntemp)))
    four+=[(temp[-2][1],temp[-3][1],temp[-1][1],"t"+str(ntemp))]
    temp = temp[:-2]
    temp += [(temp[-1][0],"t"+str(ntemp), temp[-1][2])]
    ntemp += 1
    return 0

def fun_33():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    temp += [("右项", -1, -1)]
    return 0

def fun_34():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    t = goon(2)
    return t


def fun_35():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(2)
    return 0

def fun_36():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(2)
    return 0

def fun_37():
    global Parser_r1, Parser_r2, temp,ntemp,four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(2)
    goon(1)
    print(("j==", temp[-1][1], 0, "to"))
    four += [("j==", temp[-1][1], 0, "to")]
    k = len(four)
    goon(2)
    goon(2)
    goon(1)
    four += [("j","_","_","to")]
    four[k-1] = (four[k-1][0],four[k-1][1],four[k-1][2],len(four))
    k = len(four)
    goon(2)
    goon(1)
    four[k - 1] = (four[k - 1][0], four[k - 1][1], four[k - 1][2], len(four))
    temp = temp[:-8]
    temp += [("条件语句",1,-1)]
    return 0

def fun_38():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    temp += [temp[-1]]
    return 0

def fun_39():
    global Parser_r1, Parser_r2, temp,four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(2)
    goon(1)
    goon(2)
    temp = temp[:-4]
    temp+=[("条件语句2",-1,-1)]
    return 0

def fun_40():
    global Parser_r1, Parser_r2, temp, ntemp, four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(1)
    print(("!",temp[-1][1],"_",temp[-1][1]))
    four +=[("!",temp[-1][1],"_",temp[-1][1])]
    temp [-2] = temp[-1]
    temp =temp[:-1]
    return 0

def fun_41():
    global Parser_r1, Parser_r2, temp, ntemp, four
    Parser_r1 = Parser_r1[1:]
    goon(1)
    return 0

def fun_42():
    global Parser_r1, Parser_r2, temp, ntemp, four
    Parser_r1 = Parser_r1[1:]
    n_start_for = len(four)
    goon(2)
    goon(2)
    goon(1)
    goon(2)
    goon(1)
    print(("j==",temp[-1][1],0,""))
    four += [("j==",temp[-1][1],0,"")]
    k=len(four)
    goon(2)
    goon(1)
    goon(2)
    goon(2)
    goon(1)
    goon(2)
    four+=[("j","_","_",n_start_for)]
    four[k - 1] = (four[k - 1][0], four[k - 1][1], four[k - 1][2], len(four))
    temp = temp[:-11]
    temp += [("for循环", -1, -1)]
    return 0

def fun_43():
    global Parser_r1, Parser_r2, temp, ntemp, four
    Parser_r1 = Parser_r1[1:]
    n_start_for = len(four)
    goon(2)
    goon(2)
    goon(1)
    print(("j==",temp[-1][1],0,""))
    four += [("j==",temp[-1][1],0,"")]
    k = len(four)
    goon(2)
    goon(2)
    goon(1)
    goon(2)
    four += [("j", "_", "_", n_start_for)]
    four[k - 1] = (four[k - 1][0], four[k - 1][1], four[k - 1][2], len(four))
    temp = temp[:-7]
    temp += [("while循环", -1, -1)]

def fun_44():
    global Parser_r1, Parser_r2, temp,four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(2)
    goon(2)
    goon(2)
    goon(1)
    goon(2)
    goon(2)
    four+=[("SCANF",temp[-3][1],"_","_")]
    temp=temp[:-7]
    return 0

def fun_45():
    global Parser_r1, Parser_r2, temp,four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(2)
    goon(2)
    goon(2)
    goon(1)
    goon(2)
    goon(2)
    four+=[("PRINT",temp[-3][1],"_","_")]
    temp=temp[:-6]
    return  0

def fun_46():
    global Parser_r1, Parser_r2, temp, four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(1)
    temp [-2] =temp [-1]
    temp=temp[:-1]
    temp[-1] = [temp[-1][0],-temp[-1][1],temp[-1][2]]
    return 0

def main():
    global temp, Parser_r1, Parser_r2 ,ntemp,four
    four ,temp = [],[]
    ntemp = 0
    Parser_r1,Parser_r2 = Parser.main()
    print("******************    语 义 分 析  *******************")
    goon(1)
    print(Parser_r1)
    print(Parser_r2)
    print(temp)

    print("********************    四 元 式   *********************")
    for i in four:
        print(i)
    return four

if __name__ == "__main__":
    main()