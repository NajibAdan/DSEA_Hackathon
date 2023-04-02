FROM python:3.9
# Environment Varaibles
ENV DISPLAY=:10
# Firefox Setup
RUN wget https://ftp.mozilla.org/pub/mozilla.org/firefox/releases/45.0.2/linux-x86_64/en-US/firefox-45.0.2.tar.bz2
RUN tar -xjvf firefox*.tar.bz2
RUN mv firefox /opt/firefox
RUN ln -sf /opt/firefox/firefox /usr/bin/firefox
# xvfb install
RUN apt-get update -y
RUN apt-get install -y python3-pip build-essential python3-dev
RUN apt-get install -y xvfb


# Make work directory
RUN mkdir /app
WORKDIR /app
ADD . /app
# Install requirements
RUN pip install -r requirements.txt
CMD ["Xvfb", ":10", "-ac"]
CMD ["python","./main.py"]