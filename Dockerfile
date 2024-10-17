##USE THE OFFICIAL Python 3.9 image

FROM python:3.9

## et the working directory to /code

WORKDIR /code

## copy the current directory content in the container at /code

COPY ./requirements.txt /code/requirements.txt

##install the requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

## setup a new user named "user"

RUN useradd user

#switch to the "user"  user

USER user

# set the home to user home directory

ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

#set the working directory to user's home directory

WORKDIR $HOME/app

#COPY THE current directory content into the container at $HOME/app SETTING THE Owner to

COPY --chown=user . $HOME/app

#START THE FASTAPI app on port 7860

CMD ["uvicorn","app:app","--host","0.0.0.0","--port","7860"]








