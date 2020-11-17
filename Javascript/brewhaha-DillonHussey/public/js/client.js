

let win;
let fps = 60; //Frames per second
let imgWidth = 0;
let imgHeigh = 0;
let img;
let boxes = [];

class Boxmaker{
    constructor(r, g, b, x, y){
        this.r = r;
        this.g = g;
        this.b = b;

        this.color = color(r,g,b)

        this.posX = x;
        this.posY = y;
        //this.posZ = brightness(color(r,g,b))*2
        //this.posZ = hue(color(r,g,b))*2
        this.posZ = brightness(color(r,g,b))*2
    }
    getR() {return this.r;}
    getG() {return this.g;}
    getB() {return this.b;}
    

    getPosX() { return this.posX}
    getPosY() { return this.posY}
    getPosZ() { return this.posZ}
    
    getColor() {return this.color}
}


function preload() {
    img = loadImage('img/dog.jpg');
    
    
}

function setup() {
    rectMode(CENTER);
    win = {width: 1000, height: 1000};
    pixelDensity(1);
    let canvas = createCanvas(win.width, win.height, WEBGL);
    canvas.parent('sketch-holder');



    frameRate(fps);


    img.loadPixels();


    //Set scale depending on dimensions of image. (small images work best ~ 100x100  needs scale 1)
    let scale = 1
   
    for(let i = 0; i < img.pixels.length; i+=4*scale) {
        boxes.push(new Boxmaker(img.pixels[i], img.pixels[i+1], img.pixels[i+2], (i % (img.width*4))/scale, Math.floor(i/(img.width))/scale ))
    }

    


}

function draw(){
    background(100);

    //console.log(boxes[150].getColor())
    
    for(let p = 0; p<boxes.length; p++){
        push();
        let b = boxes[p];
        translate(b.getPosX()-400, b.getPosY()-400, b.getPosZ());
        //stroke(b.getColor());
        noStroke();
        fill(b.getColor());
        box(4);

        pop();
    }
        

    orbitControl();
}