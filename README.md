# Vaccine Alarm

Check for Vaccine availability in a district at specified intervals and sends a message on your mobile phone when it finds a slot. Added functionalities are mentioned in the Usage.

-   [Vaccine Alarm](#vaccine-alarm)
    -   [Usage](#usage)
        -   [Install Dependencies](#install-dependencies)
        -   [Setup twilio account](#setup-twilio-account-to-enable-message-service)
        -   [Run checker](#run-checker)

## Usage

Get your district ID [here](DISTRICT_CODES.md)

```
Usage: check.py [OPTIONS]

  Checks for Vaccine availablity in a district at specified intervals and
  sounds a loud alarm when a slot ia available.

Options:
  -id, --district-id INTEGER  District ID from Cowin API, Get your district ID
                              at http://bit.ly/districtid  [required]

  -d, --delay INTEGER         Delay between each request (in seconds).
                              Default: 60 sec

  -l, --age-limit INTEGER     Minimum age limit, Eg. 18 will trigger only for
                              above 18. Default: 18

  -b, --blacklist INTEGER     Pincodes to exclude in your district, will not
                              trigger for these pincodes.

  -s, --min-seats INTEGER     Minimum number of seats to ensure for trigger.
                              Default: 1

  -dt, --dose-type INTEGER    Type of dose to get
                              Default : 1

  -w,  --whitelist INTEGER    To search for only the specified districts for the vaccine
                              slots.
  
  -vt, --vacine_type STR      Type of vaccine to search. Either COVISHIELD or COVAXIN.
                              Default : COVISHIELD

  -h, --help                  Show this message and exit.
```

### Install Dependencies

```bash
pipenv install
```

or

```bash
pip install -r vaccine-alarm-master/requirements.txt
```

### Setup Twilio account to enable message service

- Go to https://www.twilio.com/
- Sign up for a new account as a free trial
- Verify using the mobile number you want to send the notification messages to
- Go to console and get a trial number
- Copy and paste the "Accound Sid" and the "Auth Token" from the console in check.py and twilioFile.py files(in the vaccine-alarm-master/src folder)
- Change the "to_number" and "from_number" numbers to the number you want to send notifications to and the trial number respectively, in both check.py and twilioFile.py files.
- Run "python twilioFile.py" in vaccine-alarm-master folder to check that you are able to recieve the message on your mobile successfully. If not, put up an issue or checkout the twilio's website.

### Run checker

```bash
python src/check.py
```
