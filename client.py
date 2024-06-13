import socket
import threading

# Sunucunun IP adresi ve port numarası
SERVER = '127.0.0.1'
PORT = 5555

def receive_message(client_socket):
    # Sunucudan gelen mesajları dinleyen fonksiyon
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            # Hata oluştuğunda bağlantıyı kapat
            client_socket.close()
            break

def start_client():
    # İstemci soketi oluşturulur
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER, PORT))

    # Kullanıcı adı istenir ve sunucuya gönderilir
    username = input("Kullanıcı adınızı girin: ")
    client_socket.send(username.encode())

    # İstemciye hizmet vermek üzere bir iş parçacığı başlatılır
    receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
    receive_thread.start()

    # İstemci tarafından girilen mesajlar sunucuya gönderilir
    while True:
        message = input()
        client_socket.send(message.encode())

if __name__ == "__main__":
    start_client()
