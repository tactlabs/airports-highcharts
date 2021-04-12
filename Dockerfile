# Use the LTS release.
FROM python:3.8-stretch

#RUN useradd --user-group --create-home --shell /bin/false app 
  
ENV HOME=/home/app

WORKDIR $HOME/tact_charts

ADD requirements.txt $HOME/tact_charts/

ADD app.py $HOME/tact_charts/


RUN pip install -r requirements.txt

#USER app