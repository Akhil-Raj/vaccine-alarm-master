import requests
from pprint import pprint
from datetime import date
import time
import click
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC4f20b5df995843f5b73d443a4bc321db"
# Your Auth Token from twilio.com/console
auth_token  = "6c6f842638b2fbaa94769c48c294ab9b"
to_number = "+919045907963"
from_number = "+13392934573"

client = Client(account_sid, auth_token)

def play_alarm(count: int):
    for _ in range(count):
        print("BINGO@!!")


def sleep_with_progress(seconds: int):
    for _ in range(seconds):
        print(".", flush=True, end="")
        time.sleep(1)
    print()


def check(district_id, age_limit, pincode_blacklist, min_seats, whitelist, dose_type\
    , vaccine_type):
    pincode_blacklist = set(pincode_blacklist)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Origin': 'https://www.cowin.gov.in',
        'Connection': 'keep-alive',
        'Referer': 'https://www.cowin.gov.in/',
        'TE': 'Trailers',
        'If-None-Match': 'W/"29da8-hpVXpOen2PnjOlRfXqrEVF7FjX4"',
    }

    params = (
        ('district_id', district_id),
        ('date', date.today().strftime("%d-%m-%Y")),
    )
    try:
        response = requests.get(
            'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict',
            headers=headers,
            params=params,
        )
    except Exception:
        print("ERROR")

    found = False
    for center in response.json()["centers"]:
        for session in center["sessions"]:
            #print(session["available_capacity"])
            if session["min_age_limit"] <= age_limit and center["pincode"] not in pincode_blacklist\
            and (whitelist == (0,) or center["pincode"] in whitelist) and \
            session["available_capacity_dose" + str(dose_type)] > min_seats and \
            session["vaccine"] == vaccine_type:
                found = True
                msg = (center["name"] + "," + str(center["pincode"]) + " has " +
                        str(session["available_capacity"]) + " vaccine slots for " + str(session["vaccine"]))
                print(msg)
                #message = client.messages.create(to="+919599269442", from_="+13392934573", body=msg)
                #print(message.sid)
                message = client.messages.create(to=to_number, from_=from_number, body=msg)
                print(message.sid)
                exit(0)

    if not found:
        print("Could not find any slots.")
    #else:
    #    play_alarm(5)
    return response


@click.command("check.py",
               context_settings={
                   "help_option_names": ['-h', '--help']
               })
@click.option("--district-id",
              "-id",
              prompt="District id",
              required=True,
              help="District ID from Cowin API, Get your district ID at http://bit.ly/districtid",
              type=int)
@click.option("--delay",
              "-d",
              help="Delay between each request (in seconds). Default: 30 sec",
              default=4)
@click.option("--age-limit",
              "-l",
              help="Minimum age limit, Eg. 18 will trigger only for above 18. Default: 18",
              default=18)
@click.option("--dose_type",
              "-dt",
              help="What kind of dose do you want? Default : 1",
              default=1)
@click.option("--blacklist",
              "-b",
              multiple=True,
              help="Pincodes to exclude in your district, will not trigger for these pincodes.",
              type=int)
@click.option("--whitelist",
              "-w",
              multiple=True,
              help="Search for only specific pincodes in your district.",
              type=int,
              default = [0])
@click.option("--min-seats",
              "-s",
              help="Minimum number of seats to ensure for trigger. Default: 1",
              default=1)
@click.option("--vaccine_type",
              "-vt",
              type=str,
              help="Type of vaccine. Default: COVISHIELD",
              default="COVISHIELD")
def main(district_id, delay, age_limit, blacklist, min_seats, whitelist, dose_type, vaccine_type):
    """
    Checks for Vaccine availablity in a district at specified intervals
    and sounds a loud alarm when a slot ia available.
    """
    print("Values provided : \n district_id = {} \n delay = {} \n age_limit = {} \
        \n blacklist = {} \n min_seats = {} \n whitelist = {} \n dose_type = {}\n \
vaccine-type = {}"\
        .format(district_id, delay, age_limit, blacklist, min_seats, whitelist, dose_type, vaccine_type))
    while True:
        check(district_id, age_limit, blacklist, min_seats, whitelist, dose_type, vaccine_type)
        print(f"Sleeping for {delay} seconds")
        sleep_with_progress(delay)


if __name__ == "__main__":
    main()
