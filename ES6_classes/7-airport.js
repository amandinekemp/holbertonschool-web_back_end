export default class Airport {
  // Declaring the constructor
  constructor(name, code) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a String');
    }
    if (typeof code !== 'string') {
      throw new TypeError('Code must be a String');
    }
    // Initializing the attributes with an underscore
    this._name = name;
    this._code = code;
  }

  // Getter for the name attribute
  get name() {
    return this._name;
  }

  set name(value) {
    this._name = value;
  }

  // Getter for the code attribute
  get code() {
    return this._code;
  }

  set code(value) {
    this._code = value;
  }

  // Overriding the toString method to return the airport code
  toString() {
    return `[object ${this._code}]`;
  }
}
