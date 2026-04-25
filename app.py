from flask import Flask, render_template, request
from core.parser import LogParser

app = Flask(__name__)
parser = LogParser()

def get_ai_advice(analysis):
    # Basit bir AI mantığı simülasyonu
    high_risks = [item for item in analysis if item['risk'] == 'High']
    if high_risks:
        return "⚠️ KRİTİK: Yüksek riskli IP'ler tespit edildi. Incident Response (IR) sürecini başlatın ve bu IP'leri Firewall üzerinden izole edin."
    return "✅ TEMİZ: Analiz edilen trafik normal görünüyor. Rutin log takibi yeterlidir."

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    log_input = ""
    ai_note = ""
    
    if request.method == 'POST':
        log_input = request.form.get('log_data')
        if log_input:
            results = parser.parse_log(log_input)
            ai_note = get_ai_advice(results['analysis'])
    
    html_template = f"""
    <html>
        <head>
            <title>LogSentry v1.0</title>
            <style>
                body {{ background: #0d1117; color: #c9d1d9; font-family: 'Segoe UI', sans-serif; padding: 40px; }}
                .container {{ max-width: 900px; margin: auto; }}
                h1 {{ color: #58a6ff; display: flex; align-items: center; justify-content: space-between; }}
                .badge {{ background: #238636; color: white; font-size: 12px; padding: 4px 8px; border-radius: 12px; }}
                textarea {{ background: #161b22; color: #d1d5db; border: 1px solid #30363d; width: 100%; border-radius: 6px; padding: 15px; font-family: monospace; }}
                button {{ background: #238636; color: white; border: none; padding: 12px 24px; border-radius: 6px; cursor: pointer; font-weight: bold; margin-top: 15px; }}
                .card {{ background: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 20px; margin-top: 25px; }}
                .ai-box {{ background: #1c2128; border-left: 4px solid #58a6ff; padding: 15px; margin-top: 20px; font-style: italic; color: #adbac7; }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 15px; }}
                th, td {{ text-align: left; padding: 12px; border-bottom: 1px solid #30363d; }}
                .risk-high {{ color: #ff7b72; font-weight: bold; }}
                .risk-medium {{ color: #ffa657; }}
                .risk-low {{ color: #7ee787; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🛡️ LogSentry <span class="badge">Blue Team Edition</span></h1>
                <form method="post">
                    <textarea name="log_data" rows="8" placeholder="Logları buraya yapıştırın...">{log_input}</textarea>
                    <button type="submit">ANALİZİ BAŞLAT</button>
                </form>
    """

    if results:
        table_rows = "".join([f"<tr><td>{i['ip']}</td><td class='risk-{i['risk'].lower()}'>{i['risk']}</td><td>{i['note']}</td></tr>" for i in results['analysis']])
        
        html_template += f"""
                <div class="card">
                    <h3>🔍 Analiz Bulguları</h3>
                    <table>
                        <thead><tr><th>IP ADRESİ</th><th>RİSK</th><th>İSTİHBARAT NOTU</th></tr></thead>
                        <tbody>{table_rows}</tbody>
                    </table>
                    
                    <div class="ai-box">
                        <strong>🤖 AI Analyst Advice:</strong><br>
                        {ai_note}
                    </div>
                </div>
        """

    html_template += "</div></body></html>"
    return html_template

if __name__ == '__main__':
    app.run(debug=True)