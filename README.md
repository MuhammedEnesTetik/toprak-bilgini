\# 🌱 Toprak Bilgini - Soil Classification \& Information System



\## 📌 Proje Hakkında

\*\*Toprak Bilgini\*\*, tarımda kullanılan farklı toprak tiplerinde yetişebilecek en verimli ürünü tahmin etmek ve bu ürünlerle ilgili bilgi sunmak için geliştirilmiş bir yapay zeka projesidir.  



Makine Öğrenmesi tarafında \*\*Random Forest\*\* algoritması kullanılmış, web servisi için \*\*Flask API\*\*, kullanıcı arayüzü içinse \*\*Flutter\*\* tercih edilmiştir.  

Bu sayede kullanıcılar hem web hem de mobil ortamda kolayca toprak analizi yapabilirler.  



---



\## ⚙️ Kullanılan Teknolojiler

\- \*\*Python\*\* 🐍  

\- \*\*Pandas\*\*, \*\*NumPy\*\* → Veri işleme  

\- \*\*Scikit-learn\*\* → Random Forest modeli  

\- \*\*Flask\*\* → REST API  

\- \*\*Flutter (Dart)\*\* → Mobil arayüz  

\- \*\*SQLite / JSON\*\* → Veri yönetimi  



---



\## 📊 Veri Kümesi

\- Dosya: `Toprak\_Random\_Forest.ipynb` içinde işlenmiştir  

\- Özellikler: pH, N, P, K, sıcaklık, nem vb.  

\- Hedef: Toprak tipi (örneğin: Kumlu, Tınlı, Killi vb.)  



---



\## 🚀 Kurulum ve Çalıştırma



\### 1. Makine Öğrenmesi Modeli

Modeli eğitmek için:

```bash

python flask\_api/model.py



