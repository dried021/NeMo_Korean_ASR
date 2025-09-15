import os
import csv
import librosa

#Dataset Path
DATASET_PATH="data/raw/kss"
OUTPUT_PATH="data/processed/kss"
TRANSCRIPT_PATH=os.path.join(DATASET_PATH, "transcript.v.1.4.txt")
OUTPUT_CSV=os.path.join(OUTPUT_PATH, "kss_manifest.csv")

#Read Transcript
with open(TRANSCRIPT_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

#Save CSV
with open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["audio_filepath", "text", "duration"])
    for line in lines:
        parts = line.strip().split("|")
        if len(parts) < 2:
            continue  # 형식이 잘못된 줄은 건너뜀

        audio_file, text = parts[0], parts[1]

        # 오디오 절대 경로
        audio_path = os.path.join(DATASET_PATH,  audio_file)

        # duration 계산
        try:
            #duration = librosa.get_duration(path=audio_path)
            duration = librosa.get_duration(filename=audio_path)
        except Exception as e:
            print(f"{audio_path} duration 계산 실패: {e}")
            duration = 0.0

        writer.writerow([audio_path, text, duration])

print(f"NeMo용 manifest 파일 위치: {OUTPUT_CSV}")