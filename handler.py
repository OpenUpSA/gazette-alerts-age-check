import imaplib
import datetime
import os

DAYS_SINCE_ALERT = 3

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("gazettescanary@gmail.com", os.environ["EMAIL_PASSWORD"])
mail.select("inbox")


def check(event, context):

    sent_since_date = (
        datetime.date.today() - datetime.timedelta(DAYS_SINCE_ALERT)
    ).strftime("%d-%b-%Y")

    result, uids = mail.uid(
        "search", None, f'(SENTSINCE {sent_since_date} HEADER Subject "Open Gazettes")'
    )

    response = {
        "headers": {"Content-Type": "text/html"},
        "body": f"{len(uids)} since {sent_since_date} ({DAUS_SINCE_ALERT} ago).",
    }
    if uids:
        response["statusCode"] = 200
    else:
        response["statusCode"] = 500

    return response
