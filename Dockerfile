FROM kylemanna/openvpn

#Install python3
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    rm -r /root/.cache

#Install dependancies
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

#Copy app code over to container and set work area
RUN mkdir /app
COPY . /app
WORKDIR /app

EXPOSE 5000

ENV FLASK_APP=ovpnWebman
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]
#entrypoint [ "FLASK_APP=ovpnWebman flask run" ]
