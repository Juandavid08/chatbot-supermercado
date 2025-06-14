import re

def validar_identificacion(ident: str) -> bool:
    return bool(re.fullmatch(r"\d{4,11}", ident))


def validar_nombre(nombre: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{1,100}", nombre))


def validar_telefono(telefono: str) -> bool:
    return bool(re.fullmatch(r"[36]\d{9}", telefono))


def validar_correo(correo: str) -> bool:
    return "@" in correo and len(correo) <= 100
