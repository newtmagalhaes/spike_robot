FROM python:alpine3.19

WORKDIR /rpa

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY remote.robot .

ENTRYPOINT [ "robot", "--rpa", "remote.robot" ]
