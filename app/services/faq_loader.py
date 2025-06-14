import pandas as pd
from docx import Document
from PyPDF2 import PdfReader
import os

def cargar_faqs() -> list:
    faqs = []

    # Ruta base relativa
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data"))

    # --- 1. Leer Horarios.xlsx ---
    try:
        horarios_path = os.path.join(base_path, "Horarios.xlsx")
        df = pd.read_excel(horarios_path)
        for _, row in df.iterrows():
            for col in row.index:
                faqs.append(str(row[col]))
    except Exception as e:
        print(f"[!] Error al leer Horarios.xlsx: {e}")

    # --- 2. Leer Preguntas_Frecuentes.docx ---
    try:
        docx_path = os.path.join(base_path, "Preguntas_Frecuentes.docx")
        doc = Document(docx_path)
        for para in doc.paragraphs:
            if para.text.strip():
                faqs.append(para.text.strip())
    except Exception as e:
        print(f"[!] Error al leer Preguntas_Frecuentes.docx: {e}")

    # --- 3. Leer Suma_Gana.pdf ---
    try:
        pdf_path = os.path.join(base_path, "Suma_Gana.pdf")
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                faqs.append(text.strip())
    except Exception as e:
        print(f"[!] Error al leer Suma_Gana.pdf: {e}")

    return faqs

if __name__ == "__main__":
    faqs = cargar_faqs()
    print(f"Total de entradas cargadas: {len(faqs)}\n")
    for i, faq in enumerate(faqs[:10]):
        print(f"{i+1}. {faq}\n")
