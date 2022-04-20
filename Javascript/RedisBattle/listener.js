// Listen to Redis and show how many items are in 
// the queue

// Connect to the redis server
const redis = require("redis");
var redisConf = {
  host: 'ev-compsci-01.principia.local', // The redis's server ip 
  port: '6379'
  }; 
const client = redis.createClient(redisConf);
client.on("error", function(error) {
  console.error(error);
});


// Loop through the following function and refresh the screen
function showQueue() {
    console.clear();

    client.lrange('LydDiltoConvert', 0, 100, (err, items) => {
        if (!err) {
            // Loop through entries and draw to screen
            for(let i = 0; i < items.length; i++) {
                console.log(items[i]);
            }
        }
    });
    // Wait a second and do it again
    setTimeout(showQueue, 1000);
}



showQueue();