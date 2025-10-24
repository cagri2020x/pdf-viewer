import os
import shutil
import json

# === AYARLAR ===
SOURCE_FOLDER = r"C:\Users\cagri\OneDrive\Masaüstü\pdf yükle"  # Kaynak klasör
TARGET_ROOT = r"C:\Users\cagri\OneDrive\Masaüstü\pdf-viewer\pdfs"  # Hedef klasör
JSON_FILE = r"C:\Users\cagri\OneDrive\Masaüstü\pdf-viewer\data.json"  # Çıktı JSON

# === KLASÖRLERİ OLUŞTUR ===
os.makedirs(TARGET_ROOT, exist_ok=True)

# === VERİ TOPLAMA ===
folders_data = []

print("PDF'ler taranıyor ve kopyalanıyor...")

for folder_name in os.listdir(SOURCE_FOLDER):
    folder_path = os.path.join(SOURCE_FOLDER, folder_name)
    
    # Sadece klasörleri işle
    if not os.path.isdir(folder_path):
        continue
    
    # Hedef klasör oluştur
    target_folder = os.path.join(TARGET_ROOT, folder_name)
    os.makedirs(target_folder, exist_ok=True)
    
    # PDF'leri bul
    pdf_files = []
    for file in os.listdir(folder_path):
        if file.lower().endswith('.pdf'):
            src_file = os.path.join(folder_path, file)
            dst_file = os.path.join(target_folder, file)
            
            # Kopyala (zaten varsa üzerine yaz)
            shutil.copy2(src_file, dst_file)
            pdf_files.append(file)
            print(f"Kopyalandı: {file} → pdfs/{folder_name}/")
    
    # JSON için veri ekle
    if pdf_files:
        folders_data.append({
            "folder": folder_name,
            "pdfs": pdf_files
        })

# === JSON DOSYASINI YAZ ===
with open(JSON_FILE, 'w', encoding='utf-8') as f:
    json.dump(folders_data, f, ensure_ascii=False, indent=2)

print(f"\nBaşarıyla tamamlandı!")
print(f"   • {len(folders_data)} klasör işlendi")
print(f"   • data.json oluşturuldu: {JSON_FILE}")
print(f"   • PDF'ler buraya kopyalandı: {TARGET_ROOT}")
print("\nŞimdi GitHub'a yükleyebilirsin!")