FROM python:3.8

ENV PYTHONUNBUFFERED 1

#COPY playbooks/keys /root/.ssh
#RUN chown -R root:root /root/.ssh
#RUN  echo "    IdentityFile ~/.ssh/id_rsa" >> /etc/ssh/ssh_config
#RUN touch /root/.ssh/known_hosts
#RUN chmod 700 /root/.ssh
#RUN chmod 600 /root/.ssh/*
#RUN ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts
#RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

RUN mkdir -p /var/log/{{ cookiecutter.github_project_name }}/
WORKDIR /code

COPY requirements.txt /tmp
WORKDIR /tmp
RUN echo "Installing requirements"
RUN pip install -r requirements.txt
ENV PYTHONPATH "/code:${PYTHONPATH}"

WORKDIR /code
ENTRYPOINT [ "/usr/local/bin/gunicorn", "-w", "18", "-b", "0.0.0.0:8000", "{{ cookiecutter.project_slug }}.wsgi:application" ]
