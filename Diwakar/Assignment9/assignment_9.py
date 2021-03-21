import requests
from datetime import datetime
from datetime import timedelta
import logging

logging.basicConfig(filename='api_calls.txt', format='%(asctime)s:%(levelname)s:%(funcName)s:::::%(message)s',
                    level=logging.DEBUG)


def get_request(url, timeout):
    flag = None
    logging.info('Get call for URL {}'.format(url))
    time_to_wait = datetime.now() + timedelta(seconds=timeout)
    while datetime.now() < time_to_wait:
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                flag = True
                logging.debug("API get call is successfull with response {}".format(response.text))
                print(response.text)
                break
            elif response.status_code in [404, 400, 401]:
                flag = True
                logging.exception('API get call failed with response {}'.format(response.text))
                print(response.text)
                break
        except Exception as e:
            logging.exception(e)

    if not flag:
        logging.exception('API call not completed within specified time')


def post_request(url, body):
    response = requests.post(url, data=body)

    if response.status_code == 201:
        logging.debug('API post call is successful with response {}'.format(response.json()))
    else:
        logging.error('API post call is not successful and response is {}'.format(response.json()))


def del_request(id):
    url = 'https://reqres.in/api/users/{}'.format(id)
    response = requests.delete(url)
    if response.status_code == 204:
        logging.debug("User of id {} deleted".format(id))
    else:
        logging.error('Error in deleting User of id {}'.format(id))


url_get = "https://reqres.in/api/users?delay=1"
url_post = "https://reqres.in/api/users"
data = {'name': 'diwakar',
        'job': 'software engineer'}
headers = {'Content-Type': 'application/json'}
post_request(url=url_post, body=data)
get_request(url_get, 10)
