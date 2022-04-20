
var express = require('express');
var formidable = require('formidable');


var app = express();
const request = require('request');
const sql = require('mssql');
const bodyParser = require('body-parser');
const fs = require('fs');

//used to create random ID
const { customAlphabet }  = require('nanoid');
const nanoid = customAlphabet('1234567890abcdef', 10);

//connect to redis server

const redis = require("redis");
var redisConf = {
  host: 'ev-compsci-01.principia.local', // The redis's server ip 
  port: '6379' //change one of these so that its not overlapping other servers? I don't think so, this is the number for redis in general. -Lydia
  }; 
const client = redis.createClient(redisConf);
client.on("error", function(error) {
console.error(error);
});


//const routes = require( "./routes" );

// Set the View Engine
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(bodyParser.raw());





// Set up the server
// process.env.PORT is related to deploying on AWS
var server = app.listen(process.env.PORT || 5000, listen);
module.exports = server;
path = require('path');


app.get('/', async(req, res) => {
  res.render('public/index', );
});


app.get('/api/upload/:fileID', async(req, res) => {
  try{
    client.lrange('LydDilcompletedFiles', 0, -1, (err,files) =>{
      if(err){ throw err}
      if (files.includes(req.params.fileID)){
        res.render('public/showGif', {ID: req.params.fileID});
        return;
      }
      else {
        res.render('public/waiting', {ID: req.params.fileID})
      }
    })
  }
  catch{
    throw err;
  }
});



app.post('/api/upload', (req, res, next) => { //
  let form = new formidable.IncomingForm();


  
  //get the form from index and add file to redis (change path, send file)
  form.parse(req, (err, fields, files) => { //files=fileName and whats being uploaded
    let oldFileA =files.someExpressFiles.path; //find old file address
    let ID = nanoid(); //unique id
    //for Dillon
    let newFile ='/Users/dillonhussey/Documents/ProgrammingLanguages/Javascript/gif-converter-2-lydia-and-dillon/From_client/'+ID //set new file address to be converted
    //For Lydia
    //let newFile = '/Users/lydia.pierce/Desktop/F20/Programming Languages/Redis/gif-converter-2-lydia-and-dillon/From_client/'+ID //Specific to Dillon
    fs.rename(oldFileA, newFile, function(err){
      if(err){
        throw err
      }
      else{
         console.log(ID);
         client.rpush(['LydDiltoConvert', ID], function(err, reply){
          //render out to please wait, send ID 
         res.render('public/waiting',{ID : ID});
          //app.get('/', async (req, res) => {
          //  console.log("Got to app.get ln 96 " + ID);
          //  res.render('public/waiting',{ID : ID});
            
          //});
        });
        /*
        //check redis done queue for completed gif files, pull down to 
        (function(){
          console.log("In redis checking function: ID: " + ID);
          setTimeout(function(){
            console.log("In redis checking function: ID: " + ID);
            gif = client.lpop('LydDilcompletedFiles')
            while (true){
              while (gif != null){
                //i'm not sure why this is necissary, is this the render?
                
                }
              setTimeout(1000);
            
                
            }
          })
        client.lpop()
        */
      //  });
      }
    });
  
    }) 
    //if(err) {
    //  next(err);
    //  return;
    //}
   // res.json({fields, newFile});
  });







// ***********************************************
// Be sure any routes are setup before this!
// Set the folder for public items
publicDir = path.join(__dirname,'public');
app.use(express.static(publicDir))
app.set('views', __dirname);
app.use(express.urlencoded({ extended: true }))

// This call back just tells us that the server has started
function listen() {
  var host = server.address().address;
  var port = server.address().port;
  console.log('Listening at http://' + host + ':' + port);
}