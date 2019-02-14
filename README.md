## Bitly url shorterer
Script that can be used to create a bitlink or to get conversion statistics for an already existing bitlink.

#### How to install
It is recommended to use [virtualenv/venv](https://docs.python.org/3/library/venv.html) to isolate the project.

You can get Access Token [here](https://app.bitly.com) at official Bitly site. Put him to your `.env` file in root folder. 

Your `.env` will looks like `TOKEN=05f23348110207rto750a678ca56a98ad3227fd9`

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```
 pip install -r requirements.txt
 ```

#### Command line Tool Examples

```
# Get new bitlink
$ python main.py <put here link you want to short>
  Your bitlink: <your bitlink>


# Get conversion statistics
$ python main.py <your bitlink>
  Total clicks: <all time total clicks>
```

#### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
