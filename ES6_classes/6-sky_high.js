import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  // Declaring the constructor
  constructor(sqft, floors) {
    // Calling the parent constructor with the sqft attribute
    super(sqft);
    // Initializing the floors attribute with an underscore
    this._floors = floors;
  }

  // Getter for the floors attribute
  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors.`;
  }
}
