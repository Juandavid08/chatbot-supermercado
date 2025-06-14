import re

def validar_identificacion(ident: str) -> bool:
    """
    4 a 11 dígitos numéricos.
    """
    return bool(re.fullmatch(r"\d{4,11}", ident))


def validar_nombre(nombre: str) -> bool:
    """
    1 a 100 letras. Se permiten tildes y la ñ.
    """
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{1,100}", nombre))


def validar_telefono(telefono: str) -> bool:
    """
    Exactamente 10 dígitos. Empieza por 3 o 6.
    """
    return bool(re.fullmatch(r"[36]\d{9}", telefono))


def validar_correo(correo: str) -> bool:
    """
    Solo valida que tenga estructura básica con arroba.
    """
    return "@" in correo and len(correo) <= 100
