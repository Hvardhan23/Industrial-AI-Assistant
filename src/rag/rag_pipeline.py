from src.rag.loader import load_documents
from src.rag.chunker import split_documents
from src.rag.embedder import get_embeddings
from src.rag.vector_store import create_vector_store
from src.rag.retriever import get_retriever

# ---------- Load Documents ----------
docs = load_documents("data/docs/Maintenance_Manual.pdf")

# ---------- Split into Chunks ----------
chunks = split_documents(docs)

# ---------- Create Embeddings ----------
embeddings = get_embeddings()

# ---------- Build FAISS ----------
vector_store = create_vector_store(
    chunks,
    embeddings
)

# ---------- Create Retriever ----------
retriever = get_retriever(vector_store)