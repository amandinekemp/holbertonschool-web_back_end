export default class HolbertonCourse {
  // Constructor of the HolbertonCourse class
  constructor(name, length, students) {
    // Check the type of the name attribute
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    // Check the type of the length attribute
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    // Check the type of the students attribute
    if (!Array.isArray(students)) {
      throw new TypeError('Students must be an array');
    }
    // Initialize the attributes of the class
    this._name = name;
    this._length = length;
    this._students = students;
  }

  // Getter for the name attribute
  get name() {
    return this._name;
  }

  // Setter for the name attribute
  set name(value) {
    // Check the type of the value assigned to name
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  // Getter for the length attribute
  get length() {
    return this._length;
  }

  // Setter for the length attribute
  set length(value) {
    // Check the type of the value assigned to length
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = value;
  }

  // Getter for the students attribute
  get students() {
    return this._students;
  }

  // Setter for the students attribute
  set students(value) {
    // Check the type of the value assigned to students
    if (!Array.isArray((value) => typeof value !== 'object')) {
      throw new TypeError('Students must be an array');
    }
    this._students = value;
  }
}
