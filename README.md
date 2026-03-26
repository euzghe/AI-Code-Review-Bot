# 🤖 Gemini AI Code Review Bot

Bu araç, **Google Gemini 3 Flash** kullanarak GitHub depolarınızdaki kodları otomatik olarak analiz eden bir **GitHub Action** motorudur.

## 🚀 Özellikler
- **Senior Developer Geri Bildirimi:** Kodunuzdaki hataları ve iyileştirme önerilerini profesyonel bir dille sunar.
- **Tam Otomatik:** Her `push` işleminde devreye girer.
- **Entegre Raporlama:** Analiz sonuçlarını doğrudan GitHub **Issues** sekmesine gönderir.

## 🛠️ Kurulum
1. Reponuzun **Settings > Secrets** kısmına `GEMINI_API_KEY` ve `GH_TOKEN` ekleyin.
2. `.github/workflows/ai-review.yml` dosyasını kendi reponuza kopyalayın.
3. Arkanıza yaslanın ve AI'nın kodunuzu incelemesini izleyin!
