import argparse

parser = argparse.ArgumentParser()

parser.add_argument('src',help="來源路徑")
parser.add_argument('dest',help="目標資料夾路徑")

args = parser.parse_args()

print('來源路徑：',args.src)