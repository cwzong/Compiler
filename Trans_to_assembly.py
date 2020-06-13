import sys
import Semantic_analysis

def trans():
    global four,result
    result = []
    four_in = [0]
    rule = {
        "j==":["判断","JE"],
        "j>":["判断","JG"],
        "j<=":["判断","JNG"],
        "j<":["判断","JL"],
        "j>=":["判断","JNL"],
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
        if rule[line[0]][0] == "判断" or rule[line[0]][0] == "转移" :
            four_in += [n]
        n = n+1

    print(four_in)
def main():
    global four
    four = Semantic_analysis.main()
    trans()

if __name__ == "__main__":
    main()