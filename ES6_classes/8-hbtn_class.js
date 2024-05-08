export default class HolbertonClass {
  // Declaring the constructor
  constructor(size, location) {
    // Initializing the attributes with an underscore
    this._size = size;
    this._location = location;
  }

  // Getter for the size attribute
  get size() {
    return this._size;
  }

  // Getter for the location attribute
  get location() {
    return this._location;
  }

  // Overriding the valueOf method to return the size attribute when cast to a Number
  valueOf() {
    return this._size;
  }

  // Overriding the toString method to return the location attribute when cast to a String
  toString() {
    return this._location;
  }
}
