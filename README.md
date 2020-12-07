# Serverless Framework AWS Python 3.6 Template

[![Serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com)
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)

<!-- [![Build Status](https://travis-ci.org/ServerlessOpsIO/%%PROJECT%%.svg?branch=master)](https://travis-ci.org/ServerlessOpsIO/%%PROJECT%%) -->

Creates a Python 3.6 Serverless Framework project for AWS.

Sets up a project with ServerlessOps project conventions. These conventions include:

- AWS profile handling
- stage handling
- Python conventions
  - directory layout
  - logging

## Usage

To use, provide the url to this repository when creating a project.

```
sls create -u https://github.com/ServerlessOpsIO/sls-aws-python-36 -p <PATH> -n <NAME>
```

### Instructions to run locally

```
$ npm install
$ sls offline
```

### To Test It Locally

- Make the following request (replace `{{URL}}` with the page you want to get content for)

```
curl -H "Content-type: application/json" -d '{"src":"es", "tgt":"en", "service":1, "texts":["Hola","Mundo"]}' -X POST http://localhost:3000/dev/translate
```

### Configure AWS Credentials

```
$ serverless config credentials --provider aws --key {{KEY}} --secret {{SECRET}}
```

### To Deploy on AWS

- Add your profile in `serverless.yml` and run

```
$ sls deploy
```

- Make the following request (replace `{{URL}}` with the page you want to get content for and `{{lambda_url}}` with your lambda url)

```
curl -H "Content-type: application/json" -d '{"src":"es", "tgt":"en", "service":1, "texts":["Hola","Mundo"]}' -X POST {{lambda_url}}
```
