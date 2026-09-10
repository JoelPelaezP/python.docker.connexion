# # Start your image with a node base image
# #FROM node:18-alpine
# FROM python:3.10.16-slim-bullseye as build
# # The /app directory should act as the main application directory
# #WORKDIR /app

# RUN pip install 'poetry~=1.8.5'
# # Copy the app package and package-lock.json file
# #COPY package*.json ./

# # Copy local directories to the current local directory of our docker image (/app)
# # COPY ./src ./src
# # COPY ./public ./public

# # Install node packages, install serve, build the app, and remove dependencies at the end
# # RUN npm install \
# #     && npm install -g serve \
# #     && npm run build \
# #     && rm -fr node_modules

# # EXPOSE 3000

# # Start the app using serve command
# # CMD [ "serve", "-s", "build" ]

# FROM build as dev
# USER root
# WORKDIR /app

# #virtual env    
# COPY pyproject.toml poetry.lock ./
# RUN poetry config virtualenvs.in-project false && poetry env use python
# # RUN poetry install --no-root --extras "api-only-dependencies"
# RUN poetry install --no-root

# COPY . ./   

# # RUN poetry install --extras "api-only-dependencies"
# RUN poetry install

# RUN ["poetry", "run", "python", "-m" , "crud"]

FROM python:3.10.16 as dev
# EXPOSE 3003
RUN pip install 'poetry~=1.8.5'
RUN apt-get update \
    && apt-get install --no-install-recommends --yes \
    libffi-dev make bsdmainutils \
    build-essential git curl \
    postgresql libpq-dev gnupg ghostscript graphviz

# ARG RUN_UID
# ARG RUN_USER

# RUN : "${RUN_USER:?RUN_USER and RUN_UID need to be set and non-empty.}" && \
#     [ "${RUN_USER}" = "root" ] || \
#     (useradd -mU --home "/home/${RUN_USER}" --uid ${RUN_UID} "${RUN_USER}" \
#     && mkdir /app \
#     && chown -R ${RUN_UID} "/home/${RUN_USER}" /app)

# USER ${RUN_USER}

# ARG RUN_USER

USER root
# COPY ./local/bashrc /home/${RUN_USER}/.bashrc
# COPY ./local/inputrc /home/${RUN_USER}/.inputrc
# RUN rm /etc/bash.bashrc

# USER ${RUN_USER}
WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.in-project false && poetry env use python
RUN poetry install --no-root
# COPY requirements.txt .
# RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . ./

RUN poetry install
# CMD [ "flask", "run", "--host", "0.0.0.0" ]
RUN ["poetry", "run", "python", "-m" , "crud"]