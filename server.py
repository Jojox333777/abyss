import http.server
import socketserver
import webbrowser
import os
import threading
import time

# Configuration du serveur
PORT = 8000
HOST = "localhost"
HTML_FILE = "index.html"  # Remplacez par le nom de votre fichier HTML si nécessaire

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Ajouter des en-têtes CORS pour permettre les requêtes
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def start_server():
    # Changer le répertoire de travail pour le dossier actuel
    web_dir = os.path.join(os.path.dirname(__file__))
    os.chdir(web_dir)
    
    # Créer le gestionnaire de serveur
    with socketserver.TCPServer((HOST, PORT), MyHTTPRequestHandler) as httpd:
        print(f"Serveur démarré sur http://{HOST}:{PORT}")
        print(f"Ouvrage automatique du fichier {HTML_FILE} dans le navigateur...")
        print("Appuyez sur Ctrl+C pour arrêter le serveur")
        
        # Ouvrir le navigateur automatiquement
        webbrowser.open_new_tab(f"http://{HOST}:{PORT}/{HTML_FILE}")
        
        try:
            # Démarrer le serveur
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nArrêt du serveur...")
            httpd.shutdown()

if __name__ == "__main__":
    start_server()