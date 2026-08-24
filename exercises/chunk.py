from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader("data/schadensfall_beispiel.txt")
dokumente = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=60, chunk_overlap=30)
chunks = splitter.split_documents(dokumente)

for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i} ---")
    print(chunk.page_content)