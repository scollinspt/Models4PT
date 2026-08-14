FROM python:3.11-slim

WORKDIR /app
ENV PYTHONUNBUFFERED=1

# Install the backend package. The frontend is deployed separately.
COPY . /app

RUN pip install --no-cache-dir setuptools==84.0.0 wheel==0.48.0
RUN pip install --no-cache-dir -r requirements.lock
RUN pip install --no-cache-dir --no-deps --no-build-isolation .

EXPOSE 8000

CMD ["uvicorn", "models4pt.app:app", "--host", "0.0.0.0", "--port", "8000"]
