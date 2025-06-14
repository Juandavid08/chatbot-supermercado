from app.services.nlp_engine import construir_bot
from app.database.db import SessionLocal
from app.database.crud import get_cliente_by_ident, create_cliente
from app.utils.validators import (
    validar_identificacion,
    validar_nombre,
    validar_telefono,
    validar_correo,
)

retriever = construir_bot()
db = SessionLocal()

print("🤖 Bienvenido al asistente virtual del supermercado.\n")

# Validacion de identificación del cliente
while True:
    identificacion = input("Ingresa tu identificación: ").strip()
    if not validar_identificacion(identificacion):
        print("❌ Identificación inválida. Debe tener entre 4 y 11 dígitos numéricos.\n")
        continue

    cliente = get_cliente_by_ident(db, identificacion)
    if cliente:
        print(f"✅ ¡Hola {cliente.nombre}! Puedes hacerme cualquier pregunta sobre nuestros servicios.\n")
        break
    else:
        print("💬 No encontré tu identificación. Vamos a registrarte.\n")

        # Pedir nombre y que cuumplas con las validaciones especificadas
        while True:
            nombre = input("Ingresa tu nombre completo: ").strip()
            if validar_nombre(nombre):
                break
            print("❌ Nombre inválido. Solo letras, máximo 100 caracteres.\n")

        # Pedir teléfonoy que cuumplas con las validaciones especificadas
        while True:
            telefono = input("Ingresa tu número de teléfono (debe iniciar por 3 o 6): ").strip()
            if validar_telefono(telefono):
                break
            print("❌ Teléfono inválido. Debe tener exactamente 10 dígitos e iniciar por 3 o 6.\n")

        # Pedir correo y que cuumplas con las validaciones especificadas
        while True:
            correo = input("Ingresa tu correo electrónico: ").strip()
            if validar_correo(correo):
                break
            print("❌ Correo inválido. Asegúrate de incluir @.\n")

        # Creacion de nuevo cliente
        nuevo_cliente = {
            "identificacion": identificacion,
            "nombre": nombre,
            "telefono": telefono,
            "correo": correo
        }

        cliente = create_cliente(db, nuevo_cliente)
        print(f"\n✅ ¡Registro exitoso! Bienvenido, {cliente.nombre}. Ahora puedes hacerme preguntas.\n")
        break

# While para interactuar con el bot
print("Puedes hacerme preguntas sobre nuestros productos, servicios o cualquier otra consulta.\n")
while True:
    mensaje = input("👤 Tú: ")
    if mensaje.lower() in ["salir", "exit", "q"]:
        print("👋 Adiós. Regresa pronto")
        break

    resultados = retriever.invoke(mensaje)

    if resultados:
        respuesta = resultados[0].page_content.strip()

        # Filtrar pregunta si viene junto a la respuesta
        lineas = respuesta.split("\n", 1)
        solo_respuesta = lineas[1] if len(lineas) > 1 else respuesta

        print(f"🤖 Bot: {solo_respuesta}\n")
    else:
        print("🤖 Bot: Lo siento, no encontré una respuesta relacionada.\n")

    print("¿Tienes otra pregunta? (Escribe 'salir' para terminar)\n")
