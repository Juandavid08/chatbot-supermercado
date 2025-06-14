from app.services.faq_loader import cargar_faqs
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document

def construir_bot():
    datos_faq = cargar_faqs()

    documentos = [Document(page_content=texto) for texto in datos_faq if texto.strip()]
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=4000,  # Aumenta el límite de caracteres por fragmento
        chunk_overlap=400
    )    
    docs = splitter.split_documents(documentos)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vector_store = FAISS.from_documents(docs, embeddings)

    retriever = vector_store.as_retriever()

    return retriever
