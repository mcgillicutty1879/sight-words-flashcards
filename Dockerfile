FROM python:3.11-slim

# Install dependencies
RUN pip install --no-cache-dir flask flask-cors gtts

WORKDIR /app
COPY app.py .
COPY static ./static

EXPOSE 5000

CMD ["python", "app.py"]
