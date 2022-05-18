#可以輸入學生成績，並找出排第二高分學生的程式。


def read_file(filename):
    score_file = []
    with open(filename, "r") as f:
        for line in f:
            if "姓名,成績" in line:
                continue
            s = line.strip().split(",")
            score_file.append(s)
    print(score_file)
    return score_file


def input_data(score_file):
    while True:
        name = input("請輸入學生姓名，不再輸入請按q結束: ")
        if name == "q":
            print("感謝使用本系統。")
            break
        score = input("請輸入學生成績: ")
        d = []
        d.append(name)
        d.append(score)
        score_file.append(d)
    print(score_file)
    return score_file


def show_score(score_file):
    for p in score_file:
        print(p[0], "的成績是", p[1])


def write_file(filename, score_file):
    with open(filename, "w") as f:
        f.write("姓名,成績\n")
        for ns in score_file:
            f.write(ns[0] + "," + ns[1] + "\n")


def sort_score(score_file):
    rank = sorted(score_file, reverse = True, key = lambda s:s[1])
    print(rank)
    print("第二高分的同學是:", rank[1][0], "他的成績是:", rank[1][1])


def main():
    filename = "score_file.csv"
    import os
    if os.path.isfile(filename):
        print("找到檔案了。")
        score_file = read_file(filename)
    else:
        print("找不到檔案。")
    score_file = input_data(score_file)
    show_score(score_file)
    write_file("score_file.csv", score_file)
    sort_score(score_file)

main()