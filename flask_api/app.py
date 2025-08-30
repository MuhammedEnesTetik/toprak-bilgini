from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import joblib
from flask_cors import CORS  # type: ignore # CORS modülü : Elimizdeki API'nin farklı bir kaynaktan gelen istekleri kabul etmesini sağlıyor

app = Flask(__name__)
CORS(app)  # CORS'u aktifleştir

# Modeli yükle
model = joblib.load(r'C:\Users\Vedat\Desktop\Github_Projeleri\Toprak_Bilgini\flask_api\model.pkl')
label_encoder = joblib.load(r'C:\Users\Vedat\Desktop\Github_Projeleri\Toprak_Bilgini\flask_api\label_encoder.pkl') #etiket kodlyıcı

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json() #json ile gelen veri alınıyor
    df = pd.DataFrame(data, index=[0]) #veri pandas ile bir dataframe dönüştürülüyor
    
    for column in df.columns:
        if df[column].dtype == object:
            df[column] = label_encoder.transform(df[column]) #verilerde metinsel ifadeler varsa bunlar dönüştürülür
    
    prediction = model.predict(df) #Tahmin
    prediction_proba = model.predict_proba(df) #olasılıksal değerin hesaplanması

    response = {
        'prediction': label_encoder.inverse_transform(prediction)[0], #sayısal tahminler etiket isimlerine dönüştürülüyor.
        'probability': round(np.max(prediction_proba) * 100, 2)
    }
    
    return jsonify(response) #json formatında bir yanıt oluştur ve gönder

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') #Uygulamanın başlatılması ve tüm ağ cihazları tarafından erişilebilir olması
