import os
import json
import librosa

# Dataset Path
DATASET_PATH = "data/raw/kss"
OUTPUT_PATH = "data/processed/kss"
TRANSCRIPT_PATH = os.path.join(DATASET_PATH, "transcript.v.1.4.txt")
OUTPUT_JSON = os.path.join(OUTPUT_PATH, "kss_manifest.json")

# 출력 디렉토리 생성
os.makedirs(OUTPUT_PATH, exist_ok=True)

# Read Transcript
with open(TRANSCRIPT_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Save JSON Manifest
with open(OUTPUT_JSON, "w", encoding="utf-8") as jsonfile:
    for line in lines:
        parts = line.strip().split("|")
        if len(parts) < 2:
            continue  # 형식이 잘못된 줄은 건너뜀

        audio_file, text = parts[0], parts[1]

        # 오디오 절대 경로
        audio_path = os.path.join(DATASET_PATH, audio_file)

        # duration 계산
        try:
            duration = librosa.get_duration(path=audio_path)
        except Exception as e:
            print(f"{audio_path} duration 계산 실패: {e}")
            duration = 0.0

        # Colab 절대 경로로 변환
        audio_path = os.path.join("/content/drive/MyDrive/NeMo_Korean_ASR", DATASET_PATH, audio_file)
        audio_path = audio_path.replace("\\", "/")

        # NeMo JSON 형식으로 저장
        manifest_entry = {
            "audio_filepath": audio_path,
            "text": text,
            "duration": duration
        }
        
        # 한 줄에 하나씩 JSON 객체 쓰기
        jsonfile.write(json.dumps(manifest_entry, ensure_ascii=False) + '\n')

print(f"NeMo용 manifest 파일 위치: {OUTPUT_JSON}")

# 사용할 때는 이 변수로
train_manifest = OUTPUT_JSON
