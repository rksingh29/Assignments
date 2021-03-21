import web_login
import json
import logging

log = logging.getLogger(__name__)

with open('loginDetails.json') as data:
    conf = json.load(data)


def login_to_fb():
    """
        Login to facebook page
    """

    myFbEmail = conf['fb_user']['email']
    myFbPassword = conf['fb_user']['password']
    myURL = conf['fb_user']['url']

    response = web_login.login(myURL, myFbEmail, myFbPassword)
    if response:
        log.info("Successfully logged into facebook!")
    else:
        log.info("Login failed!")


def logout_from_fb():
    """
    Logout from facebook page.
    """

    response = web_login.logout()
    if response:
        log.info("Successfully logged out of facebook!")
    else:
        log.info("Could not log out of facebook! Try again")
