
# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!

# My AWS CDK Project – Scheduled Lambda Canary

## What this project is about

This project uses AWS CDK with Python to set up a Lambda function that runs every 5 minutes. The Lambda (called a "canary") is meant to check on a website or resource regularly to help with monitoring.

It shows how to use infrastructure-as-code with AWS CDK, Lambda, and EventBridge (which schedules the function).

---

## How my project is set up

- The CDK stack code is in `Lokmun/lokmun_stack.py`. This is where the Lambda and the scheduled event rule are defined.
- The Lambda function code itself is in `lambda/canary.py`.
- The app entry point is `Lokmun/app.py`, which kicks off the deployment.

---

## What you need before starting

- Make sure your AWS CLI is set up with credentials (`aws configure`)
- Install AWS CDK globally (`npm install -g aws-cdk`)
- Use Python 3.9 or later — I recommend running everything in a virtual environment

---

## How to get started

This project is a standard Python project. It comes with a virtual environment in the `.venv` folder.

### To set up the virtual environment on Mac or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
