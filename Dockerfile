FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app
ENV FLASK_APP=app.app
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
CMD curl -f http://localhost:5000/health || exit 1
CMD ["flask", "run"]

