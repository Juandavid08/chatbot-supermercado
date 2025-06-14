from app.services.nlp_engine import construir_bot

retriever = construir_bot()

print("🤖 Bot listo. Escribe tu pregunta (o 'salir' para terminar)\n")

while True:
    pregunta = input("👤 Tú: ")
    if pregunta.lower() in ["salir", "exit", "q"]:
        print("👋 Adiós.")
        break

    resultados = retriever.invoke(pregunta)    
    
    if resultados:
        print(f"\n🤖 Respuesta:\n{resultados[0].page_content}\n")
    else:
        print("🤖 Lo siento, no encontré una respuesta relacionada.\n")
