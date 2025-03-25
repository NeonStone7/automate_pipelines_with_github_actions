import time
import datetime
from dotenv import load_dotenv
import os
load_dotenv()

FAKE_API_KEY = os.getenv('FAKE_API_KEY')
def run_function(function,message):
    t0 = time.time()
    function()
    t1 = time.time()
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f'{now_time}: {message} {t1-t0} seconds.')

def getVideoIDs():
    fake_key = FAKE_API_KEY
    return {1,2,3,4}

def getVideoTranscripts():
    return {'ff', 'wr'}

def transformData():
    return {1,2,3,4}

def createTextEmbeddings():
    return {1,2,3,4}