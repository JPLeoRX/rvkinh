FROM python:3.8

# Common dependencies
RUN pip install requests==2.25.1
RUN pip install fastapi==0.63.0
RUN pip install uvicorn==0.13.3
RUN pip install injectable==3.4.4
RUN pip install SQLAlchemy==1.3.23
RUN pip install yoyo-migrations==7.3.1
RUN pip install psycopg2-binary==2.8.6
RUN pip install simplestr==0.5.0
RUN pip install omoide-cache==0.1.2
RUN pip install python-multipart==0.0.5

# Main app
COPY . /app
WORKDIR /app

# Run command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9543", "--workers", "1"]