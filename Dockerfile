FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=False
ENV SECRET_KEY=dummy-secret-key-for-build
ENV ALLOWED_HOSTS=localhost,127.0.0.1,.elasticbeanstalk.com

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p logs staticfiles

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
