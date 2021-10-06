FROM python:3.8-slim

WORKDIR /app
COPY . .
EXPOSE 5000
EXPOSE 8080
RUN pip install -r requirements.txt
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]