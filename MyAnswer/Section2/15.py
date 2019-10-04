# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

fname = 'hightemp.txt'
n = int(input('N--> '))

if n > 0:
    with open(fname) as data_file:
        lines = data_file.readlines()

    for line in lines[-n:]:
        print(line.rstrip())
