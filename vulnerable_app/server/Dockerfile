FROM python:3.12-slim
WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
# run the backend
CMD ["python", "app.py"]