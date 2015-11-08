// A simple Particle class

class Particle {
  PVector Location;
  PVector Velocity;
  PVector Acceleration;
  float Lifespan;

  Particle(PVector location, PVector acceleration, float lifespan) {
    Acceleration = acceleration;
    Velocity = new PVector(random(-1,1),random(-2,0));
    Location = location.get();
    Lifespan = lifespan;
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
  }

  // Method to display
  void display() {
    stroke(0,Lifespan);
    fill(0,Lifespan);
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