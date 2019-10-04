# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

fname = 'hightemp.txt'
n = int(input('N--> '))

with open(fname) as data_file:
    for i, line in enumerate(data_file):
        if i >= n:
            break
        print(line.rstrip())
