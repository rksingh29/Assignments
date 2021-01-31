import requests

base_url = 'www.nseindia.com'
session = requests.Session()


def nse_eq_data(session, base_url):
    filename = '/api/historical/cm/equity'

    # api-endpoint
    URL = 'https://{}{}'.format(base_url, filename)

    PARAMS = {"symbol": "ICICIBANK"}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    respose = session.get(URL, params=PARAMS, headers=headers, timeout=5)
    return respose.json()


def nse_market_status(session, base_url):
    filename = '/api/marketStatus'
    URL = 'https://{}{}'.format(base_url, filename)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    respose = session.get(URL, headers=headers, timeout=5)
    return respose.json()


status = nse_market_status(session, base_url)
print(status)
'''    
/Users/rajeshsingh/Documents/Assignments/venv/bin/python /Users/rajeshsingh/Documents/Assignments/Assignment_9/test_demo_9.py
{'marketState': [{'market': 'Capital Market', 'marketStatus': 'Closed', 'tradeDate': '01-Feb-2021', 'index': 'NIFTY 50', 'last': 13634.6, 'variation': -182.9499999999989, 'percentChange': -1.32, 'marketStatusMessage': 'Normal Market has Closed'}, {'market': 'Currency', 'marketStatus': 'Closed', 'tradeDate': '01-Feb-2021', 'index': '', 'last': '', 'variation': '', 'percentChange': '', 'marketStatusMessage': 'Market is Closed'}, {'market': 'Commodity', 'marketStatus': 'Closed', 'tradeDate': '01-Feb-2021', 'index': '', 'last': '', 'variation': '', 'percentChange': '', 'marketStatusMessage': 'Market is Closed'}, {'market': 'Debt', 'marketStatus': 'Closed', 'tradeDate': '01-Feb-2021', 'index': '', 'last': '', 'variation': '', 'percentChange': '', 'marketStatusMessage': 'Market is Closed'}]}

Process finished with exit code 0

'''
