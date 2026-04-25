# 🛡️ LogSentry v1.0

**LogSentry**, siber güvenlik analistleri için geliştirilmiş hızlı bir log analiz ve tehdit istihbaratı zenginleştirme aracıdır. Ham log verilerini anlamlı bir tabloya dönüştürerek analiz sürecini hızlandırır.

## ✨ Özellikler

* **Hızlı Analiz:** Karmaşık loglar içindeki IP adreslerini otomatik olarak ayıklar.
* **Tehdit İstihbaratı:** Tespit edilen IP'lere (simüle edilmiş verilerle) risk puanı atar.
* **AI Tavsiyesi:** Analiz sonuçlarına göre olay müdahale önerileri sunar.
* **Modern Arayüz:** Karanlık mod destekli, sade ve etkili bir dashboard.

## 🛠️ Kurulum ve Çalıştırma

```bash
# Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt

# Uygulamayı başlatın
python app.py

Uygulama çalıştıktan sonra tarayıcınızdan http://127.0.0.1:5000 adresine girerek kullanmaya başlayabilirsiniz.

📁 Proje Yapısı
core/: Analiz motoru ve istihbarat katmanı.

logs/: Örnek log dosyaları.

app.py: Web arayüzü ve ana uygulama.

README.md: Kullanım kılavuzu.

🎯 Gelecek Planları
[ ] Gerçek zamanlı API entegrasyonları (VirusTotal, AbuseIPDB).

[ ] Analiz sonuçlarını PDF olarak raporlama.

Geliştirici: Kadir Topçu
