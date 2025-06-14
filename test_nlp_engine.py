from app.services.nlp_engine import construir_bot

retriever = construir_bot()

print("🤖 Hola, escribe tu pregunta o escribe salir para terminar)\n")

while True:
    pregunta = input("👨‍💻​ Usted: ")
    if pregunta.lower() in ["Salir","salir", "exit","Exit", "q"]:
        print("👋 Adiós.")
        break

    resultados = retriever.invoke(pregunta)    
    
    if resultados:
        print(f"\n🤖 Respuesta:\n{resultados[0].page_content}\n")
    else:
        print("🤖 Lo siento, no encontré una respuesta relacionada.\n")
