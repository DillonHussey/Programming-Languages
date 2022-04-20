import ffmpeg
import redis
import time

# readFiles writeFiles
path_writesFiles = '/Users/dillonhussey/Documents/ProgrammingLanguages/Javascript/gif-converter-2-lydia-and-dillon/Web-project/public/To_client/'
path_readFiles = '/Users/dillonhussey/Documents/ProgrammingLanguages/Javascript/gif-converter-2-lydia-and-dillon/From_client/'


# Connect to the redis server
client = redis.Redis(host='ev-compsci-01.principia.local', port=6379, db=0)

# Step 1: pop
itemFound = client.lpop('LydDiltoConvert') #path_readFiles + itemFound.decode("utf-8"))
#itemFound = 'Kite-Flying.MP4'

# Step 2: Convert from MOV or MP4 to .gif w/ ffmpeg
# ffmpeg -i input.mov -vf scale=w=320:h=240:force_original_aspect_ratio=decrease output.gif
while True:
    while itemFound != None: #loop until item is not found
        (
            ffmpeg
            .input(path_readFiles + itemFound.decode("utf-8"))
            .output(path_writesFiles + itemFound.decode("utf-8") + ".gif")
            .run()
        )
        client.rpush('LydDilcompletedFiles', itemFound.decode('utf-8'))
        itemFound = None
        
    itemFound = client.lpop('LydDiltoConvert')

    time.sleep(3)