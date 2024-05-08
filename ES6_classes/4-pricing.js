// Importing the Currency class
import Currency from './3-currency.js';

// Declaring the Pricing class
export default class Pricing {
  // Declaring the constructor
  constructor(amount, currency) {
    if (typeof amount !== 'number') {
      throw new TypeError('Amount must be a Number');
    }
    if (!(currency instanceof Currency)) {
      throw new TypeError('Currency must be a currency');
    }

    // Initializing the attributes with an underscore
    this._amount = amount;
    this._currency = currency;
  }

  // Getter for the amount attribute
  get amount() {
    return this._amount;
  }

  // Setter for the amount attribute
  set amount(value) {
    this._amount = value;
  }

  // Getter for the currency attribute
  get currency() {
    return this._currency;
  }

  // Setter for the currency attribute
  set currency(value) {
    this._currency = value;
  }

  // Method to display the full price
  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  // Static method to convert a price
  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
