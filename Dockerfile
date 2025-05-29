FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app
# RUN apt-get update \
#     && apt-get install -y --no-install-recommends ffmpeg
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
RUN mkdir -p /app/downloads && chmod 777 /app/downloads
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]