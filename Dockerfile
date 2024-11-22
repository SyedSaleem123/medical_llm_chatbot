FROM python:3.10.11

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
# FROM python:3.10.11-slim

# WORKDIR /app

# # Copy your application code
# COPY . .

# # Copy the requirements.txt from local environment
# COPY requirements.txt /app/

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Install missing dependencies explicitly
# RUN pip install sentence-transformers langchain-pinecone==0.0.1

# CMD ["python", "app.py"]
