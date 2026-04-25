Markdown
# 🛡️ LogSentry v1.0 - Cyber Threat Analyzer

**LogSentry**, siber güvenlik analistleri ve SOC (Security Operations Center) ekipleri için tasarlanmış, ham log verilerini anlamlandıran ve otomatik tehdit istihbaratı zenginleştirmesi yapan bir analiz aracıdır.

## 🚀 Öne Çıkan Özellikler

* **Automated Log Parsing:** Karmaşık log yığınları içinden IP adreslerini ve kritik olayları saniyeler içinde ayıklar.
* **Intelligence Enrichment:** Tespit edilen IP'leri tehdit istihbaratı veri tabanlarıyla karşılaştırarak risk skoru (High/Medium/Low) atar.
* **AI Analyst Advice:** Analiz sonuçlarına göre yapay zeka destekli olay müdahale (Incident Response) tavsiyeleri üretir.
* **Visual Dashboard:** Modern, karanlık mod destekli ve analist dostu bir arayüz sunar.
* **Blue Team Focus:** Operasyonel yükü azaltmak ve hızlı triage (önceliklendirme) yapmak için optimize edilmiştir.

## 🛠️ Kurulum

Terminalinizde sırasıyla şu komutları çalıştırın:

```bash
# Projeyi klonlayın
git clone [https://github.com/kadirtooopcu/LogSentry.git](https://github.com/kadirtooopcu/LogSentry.git)

# Proje dizinine girin
cd LogSentry

# Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt

# Uygulamayı başlatın
python app.py
📖 Kullanım
Uygulama çalıştıktan sonra tarayıcınızdan http://127.0.0.1:5000 adresine gidin.

Firewall (Sophos, Fortigate vb.) veya SIEM loglarını kutucuğa yapıştırın.

ANALİZİ BAŞLAT butonuna basarak zenginleştirilmiş sonuçları görüntüleyin.

İpucu: Test etmek için logs/example_sophos.txt dosyasındaki örnek logları kullanabilirsiniz.

🏗️ Proje Yapısı
Plaintext
LogSentry/
│── core/
│   ├── parser.py        # Log analiz motoru
│   └── intelligence.py  # Tehdit istihbaratı katmanı
│── logs/                # Örnek log veri setleri
│── app.py               # Flask Web Interface
│── requirements.txt     # Bağımlılıklar
└── README.md            # Proje dokümantasyonu
🎯 Yol Haritası (Roadmap)
[ ] Gerçek zamanlı AbuseIPDB ve VirusTotal API entegrasyonu.

[ ] Log verilerini PDF/JSON formatında dışa aktarma (Export).

[ ] Çoklu log formatı (JSON, XML, CSV) için gelişmiş parser desteği.

[ ] Dockerize edilerek konteyner üzerinde çalışma desteği.

---
`Author: Kadir Topçu`
