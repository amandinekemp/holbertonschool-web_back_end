const cloneSymbol = Symbol('clone');

class Car {
  // Declaring the constructor
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Getter for the brand attribute
  get brand() {
    return this._brand;
  }

  // Getter for the motor attribute
  get motor() {
    return this._motor;
  }

  // Getter for the color attribute
  get color() {
    return this._color;
  }

  // Method to clone the car object
  cloneCar() {
    const clonedCar = new this.constructor();
    // Copy the properties of the current instance to the new instance
    for (const key of Object.getOwnPropertyNames(this)) {
      // Ignoring the cloneSymbol property
      if (key !== cloneSymbol) {
        // Copying the property value to the new instance
        clonedCar[key] = this[key];
      }
    }

    return clonedCar;
  }
}
// Exporting the Car class
export default Car;
