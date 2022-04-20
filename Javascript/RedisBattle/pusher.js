// Listen to Redis and show how many items are in 
// the queue

const Name = "Dillon";

// Make good, random ID's
const { customAlphabet }  = require('nanoid');
const nanoid = customAlphabet('1234567890abcdef', 10);

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
function pushToQueue() {

    // Get Unique ID
    const newFileName = Name + "_" + nanoid()

    client.rpush(['BattleQueue', newFileName], function(err, reply) {
        console.log("Pushed " + newFileName);
    });
    
    // Wait a second and do it again
    setTimeout(pushToQueue, 1000);
}

pushToQueue();