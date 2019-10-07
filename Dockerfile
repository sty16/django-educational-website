FROM python:3.7.3
 
# 设置工作目录
WORKDIR /pufei
 
# 复制当前目录下的文件到工作目录
COPY . /pufei
 
# 安装pip库
RUN pip install -r requirements.txt -i -i https://pypi.tuna.tsinghua.edu.cn/simple &&\
    wget https://nodejs.org/dist/v10.16.0/node-v10.16.0-linux-x64.tar.xz &&\
    tar xf node-v10.16.0-linux-x64.tar.xz -C /opt/
ENV PATH=$PATH:/opt/node-v10.16.0-linux-x64/bin
 
# 容器启动后执行命令, 运行pufei
CMD ["python", "pufei.py"]
