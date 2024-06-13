import socket
import threading

# Kullanıcı adları ve bağlantılar için bir sözlük oluşturulur
clients = {}
# Sunucunun dinleyeceği IP adresi ve port numarası
HOST = '127.0.0.1'
PORT = 5555

def broadcast(message, sender_username):
    # Bağlı tüm istemcilere mesajı gönderen fonksiyon
    for username, client_socket in clients.items():
        if username != sender_username:
            try:
                client_socket.send(f"{sender_username}: {message}".encode())
            except:
                # Hata oluştuğunda bağlantıyı kapat
                client_socket.close()
                del clients[username]

def handle_client(client_socket):
    # İstemciden gelen kullanıcı adını ve mesajları dinleyen fonksiyon
    while True:
        try:
            username = client_socket.recv(1024).decode()
            if not username:
                continue
            clients[username] = client_socket
            print(f"[*] Yeni kullanıcı katıldı: {username}")
            while True:
                message = client_socket.recv(1024).decode()
                broadcast(message, username)
        except:
            # Hata oluştuğunda bağlantıyı kapat
            client_socket.close()
            del clients[username]
            print(f"[*] Bir istemci ayrıldı.")
            break

def start_server():
    # Sunucu soketi oluşturulur
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"[*] Sunucu {HOST}:{PORT} üzerinde dinleniyor...")

    while True:
        # Yeni bir istemci bağlantısı kabul edilir
        client_socket, client_address = server_socket.accept()
        print(f"[*] Yeni bağlantı: {client_address[0]}:{client_address[1]}")

        # İstemciye hizmet vermek üzere bir iş parçacığı başlatılır
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
