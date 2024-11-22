from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
import os
from langchain_pinecone import PineconeVectorStore
from langchain.vectorstores import pinecone 

from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] =PINECONE_API_KEY


extracted_data=load_pdf_file(data='/Data')
text_chunks=text_split(extracted_data)
embeddings = download_hugging_face_embeddings()


pc = PineconeVectorStore(api_key=PINECONE_API_KEY)

index_name = "medicalbot3"


pc.create_index(
    name=index_name,
    dimension=384, 
    metric="cosine", 
    spec=ServerlessSpec(
        cloud="aws", 
        region="us-east-1"
    ) 
) 

# Embed each chunk and upsert the embeddings into your Pinecone index.
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings, 
)
print("done ")