import socket

class ClienteTCP:
    def __init__(self, host="localhost", port=5000):
        self.host = host
        self.port = port

    def iniciar(self):
        """ Inicia el cliente TCP y permite enviar mensajes. """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((self.host, self.port))
                print(f"🔵 Conectado al servidor en {self.host}:{self.port}")

                mensaje_servidor = s.recv(1024).decode()
                print(f"📢 Servidor dice: {mensaje_servidor}")

                while True:
                    mensaje = input("💬 Mensaje (APAGAR/DESCONEXION/LISTAR): ").strip()
                    s.sendall(mensaje.encode())

                    if mensaje in ["APAGAR", "DESCONEXION", "LISTAR"]:
                        print("🔴 Cerrando conexión...")
                        break

                    respuesta = s.recv(1024).decode()
                    print(f"📩 Respuesta: {respuesta}")

            except ConnectionRefusedError:
                print("❌ No se pudo conectar al servidor.")
            except ConnectionResetError:
                print("⚠️ El servidor cerró la conexión.")

if __name__ == "__main__":
    cliente = ClienteTCP()
    cliente.iniciar()