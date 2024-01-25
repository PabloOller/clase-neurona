FROM python:3.8
RUN pip install streamlit
COPY src/* /app/
COPY images/* /app/images/
WORKDIR /app
ENTRYPOINT [ "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]