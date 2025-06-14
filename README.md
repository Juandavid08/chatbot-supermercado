# chatbot-supermercado
Chatbot para supermercado

# 🤖 Chatbot de Atención para Supermercado

Este proyecto consiste en un **asistente virtual inteligente** diseñado para un canal de atención al cliente de una empresa del sector **retail - supermercado**. El bot permite registrar clientes, validar su identidad y responder preguntas frecuentes de forma **fluida y natural**, utilizando **procesamiento de lenguaje natural (NLP)** y una base de conocimiento extraída de archivos proporcionados.

---

## 🎯 Funcionalidades principales

- Registro y validación de **clientes nuevos y frecuentes**

- Validación estricta de:
  - Identificación única (4-11 dígitos)
  - Nombre completo (solo letras)
  - Teléfono (10 dígitos, empieza en 3 o 6)
  - Correo electrónico (con arroba `@`)
- Respuesta a preguntas frecuentes mediante **embeddings semánticos** (`sentence-transformers`)
- Búsqueda contextual desde 3 archivos:
  - `Horarios.xlsx`
  - `Suma_Gana.pdf`
  - `Preguntas_Frecuentes.docx`

---

## 🚀 Tecnologías utilizadas

- **FastAPI** – Framework de desarrollo web
- **LangChain + FAISS** – Vector store y procesamiento semántico
- **HuggingFace (`sentence-transformers`)** – Embeddings NLP locales
- **SQLAlchemy + SQLite** – Persistencia de datos de clientes
- **Pydantic** – Validación de datos
- **PyPDF2 / python-docx / pandas** – Carga y análisis de archivos

---

## ⚙️ Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/chatbot-supermercado.git
cd chatbot-supermercado
```

2. Creacion de entorno virtual:

```bash
python -m venv venv
.\venv\Scripts\Activate
```

3. Insxtalar dependencias necesarais:

```bash
pip install -r requirements.txt
```

4. Probar el chatbot desde la terminal

# En la razi del proyecto ejecutar este comando en la terminal
```bash
python test_nlp_engine.py
```

5. Ejecutar la API:

```bash
uvicorn app.main:app --reload
```

6. Acceder a la documentación Swagger

 http://localhost:8000/docs