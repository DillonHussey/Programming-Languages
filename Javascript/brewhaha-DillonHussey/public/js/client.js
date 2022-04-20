
/*
Dillon Hussey
Brewhaha Project
    Uses p5 library to do basic depth mapping according to brightness of pixels.
    Maps pixels into 3d space to estimate shapes
November 17 2020
For Programming Languages with Brett Huffman
*/

let win;
let fps = 60; //Frames per second
let imgWidth = 0; 
let imgHeigh = 0;
let img;
let boxes = [];     //instantiates array for pixel being represented by a box in 3d

class Boxmaker{
    constructor(r, g, b, x, y){
        //set color to rgb
        this.color = color(r,g,b)

        this.posX = x;
        this.posY = y;
        //this.posZ = brightness(color(r,g,b))*2
        //this.posZ = hue(color(r,g,b))*2
        this.posZ = brightness(color(r,g,b))*2
    }
    //getter methods
    getPosX() { return this.posX}
    getPosY() { return this.posY}
    getPosZ() { return this.posZ}
    
    getColor() {return this.color}
}

function preload() {
    //load image
    img = loadImage('img/tunnel.jpg');
}

function setup() {
    //set up window and canvas and pixelDensity to 1
    rectMode(CENTER);
    win = {width: 1000, height: 1000};
    pixelDensity(1);
    let canvas = createCanvas(win.width, win.height, WEBGL);
    canvas.parent('sketch-holder');


    //sets framerate to 60 fps
    frameRate(fps);

    //loads pixels of image into img.pixels array
    img.loadPixels();


    //Set scale depending on dimensions of image. (small images work best ~ 100x100  needs scale 1)
    let scale = 1
   
    //run through pixel array putting pixels into boxes array. (increase by 4 as each pixel has r,b,g,a)
    for(let i = 0; i < img.pixels.length; i+=4*scale) {
        //push new boxmaker object into boxes using rbg and position in array
        boxes.push(new Boxmaker(img.pixels[i], img.pixels[i+1], img.pixels[i+2], (i % (img.width*4))/scale, Math.floor(i/(img.width))/scale ))
    }

    


}

function draw(){
    //set gray background
    background(100);
    
    //run through boxes drawing each box which reps a pixel
    for(let p = 0; p<boxes.length; p++){
        push();
        //add reference to decrease runtime
        let b = boxes[p];
        //set position to x,y,z of box object
        translate(b.getPosX()-400, b.getPosY()-400, b.getPosZ());
        //noStroke to decrease runtime
        noStroke();
        //set color
        fill(b.getColor());
        //draw box of size 4
        box(4);

        pop();
    }
        
    //allows 3d orbit control
    orbitControl();
}