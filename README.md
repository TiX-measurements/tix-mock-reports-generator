#tix-mock-reports-generator

This is a simple script aiming to generate mock data to test stuff in the system.
 
## How to install it

This is a simple python script. It is made in Python 3.5. It is strongly recommended 
to install to use VirtualEnvs to run it.
 
To install all of it's dependencies you should simply run

```bash
pip install -r requirements.txt
```

Or, if you are not using VirtualEnvs

```bash
pip3 install -r requirements.txt
```

## How to run it

The script has a built in help, with some descriptions. It has 7 required parameters 
and one optional. To execute it, simply run

```bash
python -m mock_generator
```

Or

```bash
python3 -m mock_generator
```

If you are not using VirtualEnvs

If you hit the `-h` flag, the following description should appear:

```
usage: __main__.py [-h] [-s SERVER]
                   user_id username password installation_id provider_id
                   from_time to_time

positional arguments:
  user_id               Account's id where data wil be generated
  username              Account's Username where data will be generated
  password              Account's Password where data will be generated
  installation_id       Account's installation id where data will be generated
  provider_id           Dummy provider from which all the packets will be
  from_time             Date since when to generate data
  to_time               Date until when to generate data

optional arguments:
  -h, --help            show this help message and exit
  -s SERVER, --server SERVER
                        Server URL where to hit
```
