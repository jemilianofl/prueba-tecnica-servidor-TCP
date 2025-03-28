import socket
import threading

class ServidorTCP:
    def __init__(self, host="localhost", port=5000):
        self.host = host
        self.port = port
        self.servidor_activo = True
        self.clientes = []  # Lista de clientes conectados
        self.lock = threading.Lock()  # Para manejar la concurrencia

    def manejar_cliente(self, conn, addr):
        """ Maneja la conexión de un cliente. """
        with self.lock:
            self.clientes.append(addr)  # Registrar cliente

        print(f"[NUEVO] Cliente conectado desde {addr}")
        conn.sendall("Conexión exitosa. Usa 'LISTAR' para ver clientes.".encode())

        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break  # Si no recibe datos, el cliente se desconectó

                mensaje = data.decode().strip()
                print(f"[{addr}] -> {mensaje}")

                if mensaje == "APAGAR":
                    print(f"[INFO] Cliente {addr} se ha desconectado.")
                    conn.sendall("Desconectado del servidor.".encode())
                    break
                elif mensaje == "DESCONEXION":
                    print("[SERVIDOR] Apagando servidor por solicitud remota...")
                    self.servidor_activo = False
                    conn.sendall("SERVIDOR CERRÁNDOSE...".encode())
                    break
                elif mensaje == "LISTAR":
                    clientes_str = "\n".join([f"{c[0]}:{c[1]}" for c in self.clientes])
                    conn.sendall(f"Clientes conectados:\n{clientes_str}".encode())
                elif mensaje == "hola servidor":
                    conn.sendall("HOLA CLIENTE".encode())
                else:
                    conn.sendall(f"Eco: {mensaje.upper()}".encode())

        except ConnectionResetError:
            print(f"[ERROR] Cliente {addr} cerró la conexión abruptamente.")
        finally:
            with self.lock:
                self.clientes.remove(addr)  # Remover cliente al desconectarse
            conn.close()

    def iniciar(self):
        """ Inicia el servidor y acepta conexiones hasta que se apague. """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"🔵 Servidor activo en {self.host}:{self.port}")

            while self.servidor_activo:
                try:
                    s.settimeout(1)  # Permitir interrupciones para apagar
                    conn, addr = s.accept()
                    threading.Thread(target=self.manejar_cliente, args=(conn, addr), daemon=True).start()
                except socket.timeout:
                    continue  # Revisar si el servidor sigue activo

            print("🔴 Servidor apagado.")

if __name__ == "__main__":
    servidor = ServidorTCP()
    servidor.iniciar()