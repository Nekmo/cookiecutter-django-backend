FROM python:{{ cookiecutter.python_version }} as gunicorn-build
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /var/log/{{ cookiecutter.github_project_name }}/
WORKDIR /code

COPY requirements.txt /tmp
WORKDIR /tmp
RUN echo "Installing requirements"
RUN pip install -r requirements.txt
ENV PYTHONPATH "/code:${PYTHONPATH}"

WORKDIR /code
ENTRYPOINT ["/code/entrypoint.sh"]
CMD [ "/code/start.sh" ]


FROM nginx as nginx-build
ENTRYPOINT ["nginx", "-g", "daemon off;"]


FROM rabbitmq:3-management as rabbitmq-build
RUN rabbitmq-plugins enable rabbitmq_prometheus
