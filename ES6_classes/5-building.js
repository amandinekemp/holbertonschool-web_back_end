export default class Building {
  // Declaring the constructor
  constructor(sqft) {
    if (this.constructor !== Building) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    // Initializing the attribute with an underscore
    this._sqft = sqft;
  }

  // Getter for the sqft attribute
  get sqft() {
    return this._sqft;
  }

  // Setter for the sqft attribute
  set sqft(sqft) {
    this._sqft = sqft;
  }
}
