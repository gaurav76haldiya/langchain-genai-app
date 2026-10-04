FROM ollama/ollama:latest

RUN ollama serve & \
    sleep 5 && \
    ollama pull llama3.2:3b

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install --break-system-packages -r requirements.txt

COPY app.py .

EXPOSE 8501

CMD ["sh", "-c", "ollama serve & sleep 5 && streamlit run app.py --server.address=0.0.0.0 --server.port=8501"]
