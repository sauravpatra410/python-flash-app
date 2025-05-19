FROM python
COPY . /app
WORKDIR /app
RUN requirements.txt
CMD ["python3", "app.py"]