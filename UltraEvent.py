import os
import time
import requests

# Cantidad de intentos fallidos locales (Windows)
AUTH_ATTEMPTS = 10

# Archivo que vamos a crear para pruebas de FIM
FIM_PATH = r"C:\test\malicious_test.exe"

# URL del servidor Ubuntu con Nginx (poné la IP real)
TARGET_WEB = "http://192.168.6.70"


def brute_force_local():
    print("\n=== AUTH FAILURE GENERATOR ===\n")
    for i in range(AUTH_ATTEMPTS):
        print(f"[{i+1}/{AUTH_ATTEMPTS}] Intento fallido de autenticación...")
        os.system(r'net use \\127.0.0.1\IPC$ /user:fakeuser wrongpass')
        time.sleep(1)
    print(" Autenticaciones fallidas generadas.\n")


def generate_fim_event():
    print("=== FILE INTEGRITY EVENT ===\n")
    print(f"Creando archivo sospechoso en {FIM_PATH} ...")

    os.makedirs(r"C:\test", exist_ok=True)   # crea carpeta si no existe

    with open(FIM_PATH, "w") as f:
        f.write("MALWARE_TEST_SIGNATURE_123")

    print(" Archivo creado para prueba de FIM.\n")
    time.sleep(1)


def web_attack_simulation():
    print("=== WEB REQUEST EVENT ===\n")
    print(f"Enviando requests sospechosas a {TARGET_WEB}...\n")

    paths = [
        "/admin",
        "/login",
        "/../../etc/passwd",
        "/shell.php",
        "/test123",
    ]

    for p in paths:
        try:
            url = TARGET_WEB + p
            print(f"Solicitando: {url}")
            requests.get(url)
            time.sleep(0.5)
        except:
            print(" No se pudo conectar (está bien, igual genera logs).")

    print("\n Requests enviadas.\n")


# === EJECUCIÓN PRINCIPAL ===
print("\n Iniciando ULTRA EVENT GENERATOR...\n")

brute_force_local()
generate_fim_event()
web_attack_simulation()

print(" Todos los eventos fueron generados. Revisa Wazuh cuando el Manager esté vivo.")
