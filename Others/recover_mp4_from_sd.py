import os
import shutil

# 📌 정리할 폴더 경로 설정 (너의 다운로드 폴더로 바꿔줘!)
folder_path = input("파일 위치")

# 📦 분류 기준
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Documents': ['.pdf', '.docx', '.xlsx', '.pptx', '.txt'],
    'Archives': ['.zip', '.rar', '.7z'],
    'Programs': ['.exe', '.msi'],
    'Music': ['.mp3', '.wav', '.flac']
}

# 📂 파일 정리하기
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    if os.path.isfile(file_path):
        ext = os.path.splitext(filename)[1].lower()
        moved = False

        for folder_name, extensions in file_types.items():
            if ext in extensions:
                target_folder = os.path.join(folder_path, folder_name)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"{filename} → {folder_name}/")
                moved = True
                break

        # 분류되지 않은 파일 처리
        if not moved:
            others_folder = os.path.join(folder_path, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, filename))
            print(f"{filename} → Others/")
