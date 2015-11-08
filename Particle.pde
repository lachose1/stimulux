// A simple Particle class

class Particle {
  PVector Location;
  PVector Velocity;
  PVector Acceleration;
  float Lifespan;
  color PColor;

  Particle(PVector location, PVector acceleration, float lifespan, color pColor) {
    Acceleration = acceleration;
    Velocity = new PVector(random(-1,1),random(-2,0));
    Location = location.get();
    Lifespan = lifespan;
    PColor = pColor;
  }

  void run() {
    update();
    display();
    //println(Lifespan);
  }

  // Method to update Location
  void update() {
    Velocity.add(Acceleration);
    Location.add(Velocity);
    Lifespan -= 1.0;
    PColor = (PColor & 0xffffff) | ((int)Lifespan << 24); 
  }

  // Method to display
  void display() {
    //stroke(255,Lifespan);
    //fill(255,Lifespan);
    stroke(PColor);
    fill(PColor);
    ellipse(Location.x,Location.y,2,2);
  }
  
  // Is the particle still useful?
  boolean isDead() {
    if (Lifespan < 0.0) {
      return true;
    } else {
      return false;
    }
  }
}