import glob
import os.path
import random
import string
import subprocess
from pathlib import Path
from subprocess import check_call, check_output, CalledProcessError

import requests

CHUNK_SIZE = 8192
ENV_FILE = '.env'
REPLACE_FORMAT = '!!{}!!'
DEFAULT_KEY_CHARS = string.ascii_letters + string.digits
SSL_DIRECTORY = "conf/nginx/ssl"
OPTIONS_SSL_NGINX = f"{SSL_DIRECTORY}/options-ssl-nginx.conf"
SSL_DHPARAMS = f"{SSL_DIRECTORY}/ssl-dhparams.pem"
PYTHON_VERSION = '{{ cookiecutter.python_version }}'
VIRTUALENVS_DIR = Path(os.path.expanduser("~/.virtualenvs"))
GITHUB_PROJECT_NAME = '{{ cookiecutter.github_project_name }}'
USE_CELERY = {{ cookiecutter.use_celery }}
USE_YACRON = {{ cookiecutter.use_yacron }}
CREATE_VIRTUALENV = {{ cookiecutter.create_virtualenv }}


def download(url, path):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=CHUNK_SIZE):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk:
                f.write(chunk)


def generate_key(length, chars=DEFAULT_KEY_CHARS):
    return ''.join(random.choice(chars) for _ in range(length))


def replace_in_file(path, variable, value):
    with open(path, 'r+') as f:
        content = f.read().replace(REPLACE_FORMAT.format(variable), value)
        f.seek(0)
        f.write(content)
        f.truncate()


def set_secret(path, secret_key, value=None, secret_length=32, chars=DEFAULT_KEY_CHARS):
    value = value or generate_key(secret_length, chars)
    replace_in_file(path, secret_key, value)


def set_secrets(path):
    set_secret(path, 'POSTGRES_USER')
    set_secret(path, 'POSTGRES_PASSWORD')
    set_secret(path, 'SECRET_KEY', secret_length=50,
               chars='abcdefghijklmnopqrstuvwxyz0123456789!@#%^&*(-_=+)')


def download_ssl_files():
    os.makedirs(SSL_DIRECTORY, exist_ok=True)
    if not os.path.exists(OPTIONS_SSL_NGINX):
        download(
            "https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/_internal/"
            "tls_configs/options-ssl-nginx.conf",
            OPTIONS_SSL_NGINX,
        )
    if not os.path.exists(SSL_DHPARAMS):
        check_call(["openssl", "dhparam", "-out", SSL_DHPARAMS, "2048"])


def docker_separator():
    output = check_output(["docker-compose", "--version"])
    if "version 1." in output.decode():
        replace_in_file("docker-compose.develop.yml", "DOCKER_SEPARATOR", "_")
        replace_in_file(glob.glob("conf/nginx/conf.d/*.conf")[0], "DOCKER_SEPARATOR", "_")
    else:
        replace_in_file("docker-compose.develop.yml", "DOCKER_SEPARATOR", "-")
        replace_in_file(glob.glob("conf/nginx/conf.d/*.conf")[0], "DOCKER_SEPARATOR", "-")


def remove_files_dirs(file_names, dir_names):
    for file_name in file_names:
        os.remove(str(file_name))
    for dir_name in dir_names:
        os.rmdir(str(dir_name))


def remove_celery_files():
    remove_files_dirs([Path("{{ cookiecutter.project_slug }}") / "celery.py"], [])


def remove_yacron_files():
    remove_files_dirs([Path("conf") / "yacron" / "yacron.yml"], [Path("conf") / "yacron"])


def create_virtualenv():
    virtualenv_dir = VIRTUALENVS_DIR / GITHUB_PROJECT_NAME
    subprocess.run([f'python{PYTHON_VERSION}', '-m', 'venv', str(virtualenv_dir)])
    env_bin = virtualenv_dir / "bin"
    check_call([str(env_bin / 'pip'), 'install', '-U', 'pip-tools', 'pip'])
    check_call([str(env_bin / 'pip-compile')])
    check_call([str(env_bin / 'pip-compile'), 'dev-requirements.in'])
    check_call([str(env_bin / 'pip-sync'), 'requirements.txt', 'dev-requirements.txt'])
    check_call(['git', 'commit', '--allow-empty', '-m', 'Updated requirements.'])


def main():
    if not USE_CELERY:
        remove_celery_files()
    if not USE_YACRON:
        remove_yacron_files()
    set_secrets(ENV_FILE)
    download_ssl_files()
    docker_separator()
    check_call(['git', 'init'])
    try:
        check_output(['git', 'rev-list', '--count', 'HEAD'], stderr=subprocess.DEVNULL)
    except CalledProcessError:
        check_call(['git', 'commit', '--allow-empty', '-m', 'Initial commit'])
    if CREATE_VIRTUALENV:
        create_virtualenv()
    print('[?] For add a remote repo: git remote add origin <repo>')
    print('[?] Push to remote origin: git push origin master')


if __name__ == '__main__':
    main()
