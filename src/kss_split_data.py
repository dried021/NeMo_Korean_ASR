import json
import random
import os

MANIFEST_PATH = "data/processed/kss/kss_manifest.json"
DATA_DIR = "data/processed/kss"
random.seed(42)

# manifest 읽기
with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

random.shuffle(lines)
n = len(lines)
train_lines = lines[:int(0.8*n)]
val_lines   = lines[int(0.8*n):int(0.9*n)]
test_lines  = lines[int(0.9*n):]

# 파일로 저장
train_manifest = os.path.join(DATA_DIR, "train_manifest.json")
val_manifest   = os.path.join(DATA_DIR, "val_manifest.json")
test_manifest  = os.path.join(DATA_DIR, "test_manifest.json")

with open(train_manifest, "w", encoding="utf-8") as f:
    f.writelines(train_lines)
with open(val_manifest, "w", encoding="utf-8") as f:
    f.writelines(val_lines)
with open(test_manifest, "w", encoding="utf-8") as f:
    f.writelines(test_lines)

print("Train/Val/Test manifest 생성 완료!")
