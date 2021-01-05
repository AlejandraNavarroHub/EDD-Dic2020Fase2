from cryptography.fernet import Fernet
import os


def CrearLlave(nombre, ruta):
    ruta = ruta + "\\Keys\\" + str(nombre) + ".key"
    clave = Fernet.generate_key()
    with open(ruta, 'wb') as archivo:
        archivo.write(clave)


def cargar_llave(nombre, ruta):
    ruta = ruta + "\\Keys\\" + str(nombre) + ".key"
    return open(ruta, 'rb').read()


def encriptar(mensaje, llave):
    f = Fernet(llave)
    byteMessage = mensaje.encode()
    return f.encrypt(byteMessage).decode()


def desencriptar(mensaje, llave):
    f = Fernet(llave)
    return f.decrypt(mensaje.encode()).decode()


def ExisteLlave(nombre, ruta):
    ruta = ruta + "\\Keys\\" + str(nombre) + ".key"
    return os.path.isfile(ruta)


rutita = 'C:\\Users\\welma\\OneDrive\\Escritorio\\Cursos actuales\\EDD'

mensaje1 = 'Probando la compresion con llave 1'
mensaje2 = 'Probando la compresion con llave 2'
c1 = cargar_llave('Contraseña1', rutita)
c2 = cargar_llave('Contraseña2', rutita)

print(desencriptar('gAAAAABf88jU8lKFQNlBGiDA23-GH_yIX2B4r3A08MwUn6ipYZfYQPN4ROxfRqZc7J_mNzKzJDirHF6MHe5piiAAb6vYgV_qRBc5-VVWBt2fDvw4jS7YMsf7QvSgou3F18N_myXIVQi4', c1))
print(desencriptar('gAAAAABf88jUHFnG4FBcfPYqLOrMeH5pnieNxagYyK9edFeKaEpJJhlBCGP3G5F5mygK7DVRtEAG9rMtr3-In_m4ctm7zFILvckV5XopOAjFV3d4LpTskuRGwZGuDG2unE1Jj7qhOZ6B', c2))


print(ExisteLlave('ContrAseña1', rutita))
print(ExisteLlave('sgsaga', rutita))