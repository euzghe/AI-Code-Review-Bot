import os
import requests
from github import Github, Auth

# Ortam değişkenlerini al (GitHub Actions'tan gelecek)
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("GITHUB_REPOSITORY")

def analyze_file(repo, file_path):
    try:
        content = repo.get_contents(file_path).decoded_content.decode()
        print(f"🔍 {file_path} analiz ediliyor...")

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key={GEMINI_KEY}"
        
        prompt = f"Sen Senior Full-Stack Developer'sın. '{file_path}' dosyasını Türkçe analiz et, hataları ve modern iyileştirme önerilerini maddeler halinde yaz:\n\n{content}"

        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        response = requests.post(url, json=payload)
        result = response.json()

        if "candidates" in result:
            report = result["candidates"][0]["content"]["parts"][0]["text"]
            repo.create_issue(title=f"AI Code Review: {file_path}", body=report)
            print(f"✅ {file_path} için rapor oluşturuldu.")
    except Exception as e:
        print(f"⚠️ {file_path} atlandı: {e}")

def main():
    if not GITHUB_TOKEN or not GEMINI_KEY:
        print("❌ Hata: API anahtarları eksik!")
        return

    auth = Auth.Token(GITHUB_TOKEN)
    g = Github(auth=auth)
    repo = g.get_repo(REPO_NAME)
    
    # Genel olarak incelenmesini istediğimiz dosyalar
    files_to_review = ["index.html", "package.json", "src/App.jsx", "README.md"]
    
    for f in files_to_review:
        analyze_file(repo, f)

if __name__ == "__main__":
    main()
