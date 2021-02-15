# NLP Sandbox Data Node

[![GitHub Release](https://img.shields.io/github/release/nlpsandbox/data-node.svg?include_prereleases&color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/data-node/releases)
[![GitHub CI](https://img.shields.io/github/workflow/status/nlpsandbox/data-node/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/data-node/actions)
[![GitHub License](https://img.shields.io/github/license/nlpsandbox/data-node.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/data-node/blob/develop/LICENSE)
[![Docker Pulls](https://img.shields.io/docker/pulls/nlpsandbox/data-node.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/nlpsandbox/data-node)
[![Discord](https://img.shields.io/discord/770484164393828373.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=Discord&logo=discord)](https://discord.gg/Zb4ymtF "Realtime support / chat with the community and the team")
[![Coverage Status](https://img.shields.io/coveralls/github/nlpsandbox/data-node.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=coverage&logo=Coveralls)](https://coveralls.io/github/nlpsandbox/data-node?branch=)

Repository of FHIR and annotation resources used to benchmark NLP Sandbox tools

## Overview

This repository provides a Python-Flask implementation of the [NLP Sandbox Data
Node]. This Data Node relies on a MongoDB instance to store FHIR and annotation
resources used to benchmark NLP Sandbox tools.

This Data Node can be used to:

- Create and manage datasets
- Create and manage FHIR stores
  - Store and retrieve FHIR patient profiles
  - Store and retrieve clinical notes
- Create and manage annotation stores
  - Store and retrieve text annotations

### Specification

- Data Node API version: 1.0.0
- Data Node version: 1.0.0
- Docker image: [nlpsandbox/data-node]

## Usage

### Running with Docker

Create the configuration file.

    cp .env.example .env

The command below starts the Data Node locally.

    docker-compose up --build

You can stop the container run with `Ctrl+C`, followed by `docker-compose down`.

### Running with Python

We recommend using a Conda environment to install and run the Data Node.

    conda create --name data-node python=3.9.1
    conda activate data-node

Create the configuration file and export its parameters to environment
variables.

    cp .env.example .env
    export $(grep -v '^#' .env | xargs -d '\n')

Start the MongoDB instance.

    docker-compose up -d db

Install and start the Data Node.

    cd server/
    pip install -r requirements.txt
    cd server && python -m openapi_server

### Acessing the Data Node UI

The Data Node provides a web interface that you can use to create and manage
resources. The address of this interface depends on whether you run the Data
Node using Docker (production mode) or the Python development server.

- Using Docker: http://localhost/ui
- Using Python: http://localhost:8080/ui

## Contributing

Thinking about contributing to this project? Get started by reading our
[Contributor Guide](CONTRIBUTING.md).

## License

[Apache License 2.0]

<!-- Links -->

[nlpsandbox.io]: https://www.synapse.org/nlpsandbox
[NLP Sandbox]: https://www.synapse.org/nlpsandbox
[NLP Sandbox Data Node]: https://nlpsandbox.github.io/nlpsandbox-schemas/data-node/latest/docs/
[nlpsandbox/data-node]: https://hub.docker.com/r/nlpsandbox/data-node
[Apache License 2.0]: https://github.com/nlpsandbox/data-node/blob/develop/LICENSE
