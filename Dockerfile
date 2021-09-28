FROM python:3.7-slim
LABEL author="test@example.com"
RUN pip install flask==1.1.1
COPY ./server.py /server.py
ENV PORT 80
CMD ["python", "-u", "/server.py"]
