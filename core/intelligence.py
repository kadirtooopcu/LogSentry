import requests

class IntelManager:
    def __init__(self):
        self.api_key = "YOUR_API_KEY_HERE" 
        
    def check_ip(self, ip):
        """
        IP adresini simüle edilmiş bir veri tabanından kontrol eder.
        Gerçek senaryoda burası AbuseIPDB veya VT API'sine bağlanır.
        """
        # Test amaçlı bazı 'zararlı' IP senaryoları
        malicious_ips = {
            "185.123.45.67": {"risk": "High", "desc": "Known SSH Brute Force Origin"},
            "91.234.11.22": {"risk": "Medium", "desc": "Tor Exit Node - Suspected Scan"},
            "8.8.8.8": {"risk": "Low", "desc": "Google DNS - Likely Safe"}
        }
        
        return malicious_ips.get(ip, {"risk": "Unknown", "desc": "No immediate threat record found."})
