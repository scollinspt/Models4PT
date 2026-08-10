FROM python:3.11-slim

WORKDIR /app
ENV PYTHONUNBUFFERED=1

# Copy everything and install editable package plus test deps
COPY . /app

RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -e '.[test]'

EXPOSE 8000

CMD ["uvicorn", "src.models4pt.app:app", "--host", "0.0.0.0", "--port", "8000"]
