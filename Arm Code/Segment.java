//Practice file containing functions for the segments for the IK app

class Segment {
    Pvector a;
    float angle;
    float len;
    
    Pvector b = new Pvector();
    
    //Constructor
    Segment(float x, float y, float len_, float angle_){
        a = new Pvector(x,y);
        len = len_;
        angle = angle_;
    }
    void calculateB() {
        float dx = len * cos(angle);
        float dy = len * sin(angle);
        b.set(a.x+dx, a.y+dy);
        
    }
    
    void update() {
     calculateB();   
    }
    
    void show(){
        stroke(255);
        strokeWeight(4);
        line(a.x, a.y, b.x, b.y)
    }
}
