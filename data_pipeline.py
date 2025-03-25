from functions import *
import time
import datetime

now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('{now_time}: Starting pipeline now...')

# extract video ids

run_function(getVideoIDs, 'Video IDs extracted in')

########################################################

# extract video transcripts

run_function(getVideoTranscripts, 'Video transcripts extracted in')


########################################################

# transform data 

run_function(transformData, 'Data transformed in')
########################################################

# create text embeddings

run_function(createTextEmbeddings, 'Test embeddings created in')

