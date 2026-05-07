FROM python:3.13

#RUN pip install playwright

RUN mkdir /opt/test_project/
WORKDIR /opt/test_project/
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN playwright install chromium
RUN playwright install-deps

COPY *.py .
ENTRYPOINT ["pytest"]
