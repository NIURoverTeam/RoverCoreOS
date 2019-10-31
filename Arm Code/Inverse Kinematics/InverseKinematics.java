//Practice file to get segemnts moving and get used to using IK
Segment seg;

void setup() {
    size(600, 400);
    seg = new Segment(300, 200, 100, 0);
}

void draw() {
    background(51);
    seg.update();
    seg.show();
}
