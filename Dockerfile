FROM python:3.7.4

ENV HOME=/opt/utils

WORKDIR $HOME

COPY requirements.txt $HOME
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

COPY . $HOME

EXPOSE 80

ENV PYTHONUNBUFFERED=true

<<<<<<< HEAD
CMD ["python", "manage.py runserver"]
=======
CMD ["python", "manage.py runserver"]
>>>>>>> 408b83942adf5faaa05dceedd5540e6a738adefa
