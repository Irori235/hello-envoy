FROM python:3.12.0

WORKDIR /

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

COPY . .
CMD [ "python", "app.py" ]

