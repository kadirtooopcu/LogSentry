import re
from core.intelligence import IntelManager

class LogParser:
    def __init__(self):
        # IP yakalamak için regex
        self.ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        self.intel = IntelManager() # İstihbarat motorunu başlattık

    def parse_log(self, log_content):
        # Log içindeki IP'leri bul
        ips = re.findall(self.ip_pattern, log_content)
        unique_ips = list(set(ips))
        
        enriched_ips = []
        for ip in unique_ips:
            # Her IP için intelligence.py'deki check_ip fonksiyonunu çalıştır
            info = self.intel.check_ip(ip) 
            enriched_ips.append({
                "ip": ip, 
                "risk": info['risk'], 
                "note": info['desc']
            })
        
        return {
            "analysis": enriched_ips,
            "status": "Zenginleştirilmiş Analiz Tamamlandı"
        }