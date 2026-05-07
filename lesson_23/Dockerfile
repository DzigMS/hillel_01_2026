FROM openjdk:26-ea-21-slim-bookworm

RUN mkdir /opt/allure/
WORKDIR /opt/allure/

COPY ./allure-2.39.0.tgz ./
#RUN dpkg -i allure_2.39.0-1_all.deb
RUN tar -xf allure-2.39.0.tgz
RUN export PATH=$PATH:/opt/allure/allure-2.39.0/bin
RUN ln -s /opt/allure/allure-2.39.0/bin/allure /usr/bin/allure
EXPOSE 4447

ENTRYPOINT ["allure", "serve", "-h", "0.0.0.0", "--port", "4447", "/allure/report/"]