import os
import sys
import argparse

parser = argparse.ArgumentParser(description='Generate VOC trainval.txt file')

parser.add_argument('-a', '--anno_dir', default=None, help='annotation dir')
parser.add_argument('--dest_dir', default=None, type=str,
                    help='Dir to save trainval.txt')
parser.add_argument('-n', '--name', default="trainval.txt", help='annotation dir')
args = parser.parse_args()

if not os.path.exists(args.dest_dir):
    print("ERROR::DEST_DIR DOES NOT EXIST")
    sys.exit()

path = None
paths = []
anno_list = sorted(os.listdir(args.anno_dir))

f = open(os.path.join(args.dest_dir, args.name), 'w')

for i in range(len(anno_list)):
    data = str(anno_list[i][:-4]) + "\n"
    f.write(data)
f.close()