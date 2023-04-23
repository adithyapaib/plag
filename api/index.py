from http.server import BaseHTTPRequestHandler
import os, requests
from os.path import join


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("charset", "UTF-8")
        self.end_headers()
        with open(join('data','main.html'),'r') as file:
            # Send the html message
            self.responses = file.read()
            self.wfile.write(self.responses.encode())
        return
                         
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        data = self.rfile.read(int(self.headers['Content-Length']))
        burp0_url = os.environ.get('burp0_url')
        burp0_cookies = {
        "PHPSESSID": os.environ.get('PHPSESSID'),
        "first_interaction_user": os.environ.get('first_interaction_user'),
        "first_interaction_order": os.environ.get('first_interaction_order'),
        "affiliate_user": os.environ.get('affiliate_user'),
        "sbjs_migrations": os.environ.get('sbjs_migrations'),
        "sbjs_current_add": os.environ.get('sbjs_current_add'),
        "sbjs_first_add": os.environ.get('sbjs_first_add'),
        "sbjs_current": os.environ.get('sbjs_current'),
        "sbjs_first": os.environ.get('sbjs_first'),
        "sbjs_udata": os.environ.get('sbjs_udata'),
        "sbjs_session": os.environ.get('sbjs_session'),
        "_ga_788D7MTZB4": os.environ.get('ga_788D7MTZB4'),
        "_ga": os.environ.get('ga'),
        "trustedsite_visit": os.environ.get('trustedsite_visit'),
        "trustedsite_tm_float_seen": os.environ.get('trustedsite_tm_float_seen'),
        "AppleBannercookie_hide_header_banner": os.environ.get('AppleBannercookie_hide_header_banner'),
        "COOKIE_PLAGIARISM_CHECKER_TERMS": os.environ.get('COOKIE_PLAGIARISM_CHECKER_TERMS'),
        "plagiarism_checker_progress_state": os.environ.get('plagiarism_checker_progress_state')
    }
        print(burp0_url)
        burp0_headers = { "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0", "Accept": "/", "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": os.environ.get('Referer'), "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": os.environ.get('Origin'), "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "no-cors", "Sec-Fetch-Site": "same-origin", "Pragma": "no-cache", "Cache-Control": "no-cache", "Te": "trailers", "Connection": "close" }
        burp0_data = {'is_free': 'false','plagchecker_locale': 'en','product_paper_type': '1','title': '','text': str(data)}
        r = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
        self.wfile.write(r.text.encode())
        




       