let win;
let fps = 60; //Frames per second
let imgWidth = 0;
let imgHeigh = 0;
let img;

function setup() {
    rectMode(CENTER);
    win = {width: 1000, height: 1000};
    
    let canvas = createCanvas(win.width, win.height, WEBGL);
    canvas.parent('sketch-holder');

    frameRate(fps);

    //Load an image
    img = loadImage('img/bigYoshi.jpg')
}

function draw(){
    background(0);
    push();
        translate(frameCount*1,10);
        rect(10,10,50,50);
    pop();

 /*   push();
        translate(0,0,frameCount * -.5)
        rotateZ(frameCount*.01);
        rotateX(frameCount*.02);
        
        texture(img);
        sphere(400);
        
    pop();
    */

}