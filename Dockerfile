FROM python:3.6.5

ENV HOME=/opt/utils

WORKDIR $HOME

COPY requirements.txt $HOME
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt &&\
    wget https://nodejs.org/dist/v10.16.0/node-v10.16.0-linux-x64.tar.xz &&\
    tar xf node-v10.16.0-linux-x64.tar.xz -C /opt/
ENV PATH=$PATH:/opt/node-v10.16.0-linux-x64/bin

COPY . $HOME

EXPOSE 80

ENV PYTHONUNBUFFERED=true

CMD ["/bin/sh", "config/run.sh"]
