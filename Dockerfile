FROM centos
Run yum install python3 -y
RUN pip3 install pandas scikit-learn

COPY datasets/MlSummer/*  /

CMD python3 /SalaryApp.py
