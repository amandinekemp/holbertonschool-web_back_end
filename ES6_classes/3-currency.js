export default class Currency {
  // constructor of the Currency class
  constructor(code, name) {
    if (typeof code !== 'string') {
      throw new TypeError('Code must be a string');
    }
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    // Private attributes
    this._code = code;
    this._name = name;
  }

  // Getters and Setters for the class attributes

  // Code
  get code() {
    return this._code;
  }

  set code(code) {
    this._code = code;
  }

  // Name
  get name() {
    return this._name;
  }

  // Setter for the name attribute
  set name(name) {
    this._name = name;
  }

  // Method to display the name and code of the currency
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
