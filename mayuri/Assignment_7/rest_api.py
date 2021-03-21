import requests
import logging

log = logging.getLogger(__name__)

url = 'https://google.com/'


def execute_rest_apis(headers=None, data=None, params=None, method='post'):
    """

    :return:
    """
    response = None
    try:
        if method == 'post':
            response = requests.post(url, headers=headers, data=data)

        if method == 'get':
            response = requests.get(url,headers=headers, data=data, params=params)

        if method == 'put':
            response = requests.put(url, headers=headers, data=data, params=params)

        if method == 'delete':
            response = requests.delete(url, headers=headers, data=data, params=params)

        log.info(response)

        if response.status_code == 200:
            log.info('Request is successful.')
        elif response.status_code == 400:
            log.info('Bad Request.')
        elif response.status_code == 401:
            log.info('Authentication failed!')
        elif response.status_code == 403:
            log.info('Access to the specified resource is denied!')
        elif response.status_code == 404:
            log.info('The requested resource was not found on the server.')
        elif response.status_code == 500:
            log.info('Internal Server Error!')
        else:
            log.info('Something went wrong!')

    except Exception as e:
        log.exception(e)
