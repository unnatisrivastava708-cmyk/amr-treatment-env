FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn requests

EXPOSE 7860

CMD ["python", "-m", "uvicorn", "api.server:app", "--host", "0.0.0.0", "--port", "7860"]
