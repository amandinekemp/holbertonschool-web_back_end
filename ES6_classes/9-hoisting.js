export class HolbertonClass {
  constructor(year, location) {
    this._year = year;
    this._location = location;
  }

  // Getter for the year attribute
  get year() {
    return this._year;
  }

  // Getter for the location attribute
  get location() {
    return this._location;
  }
}

export class StudentHolberton {
  // Declaring the constructor
  constructor(firstName, lastName, holbertonClass) {
    // Initializing the attributes with an underscore
    this._firstName = firstName;
    this._lastName = lastName;
    this._holbertonClass = holbertonClass;
  }

  // Getter for the fullName attribute
  get fullName() {
    return `${this._firstName} ${this._lastName}`;
  }

  // Getter for the holbertonClass attribute
  get holbertonClass() {
    return this._holbertonClass;
  }

  get fullStudentDescription() {
    return `${this._firstName} ${this._lastName} - ${this._holbertonClass.year} - ${this._holbertonClass.location}`;
  }
}

// Creating instances of HolbertonClass
const class2019 = new HolbertonClass(2019, 'San Francisco');
const class2020 = new HolbertonClass(2020, 'San Francisco');

// Creating instances of StudentHolberton
const student1 = new StudentHolberton('Guillaume', 'Salva', class2020);
const student2 = new StudentHolberton('John', 'Doe', class2020);
const student3 = new StudentHolberton('Albert', 'Clinton', class2019);
const student4 = new StudentHolberton('Donald', 'Bush', class2019);
const student5 = new StudentHolberton('Jason', 'Sandler', class2019);

// Exporting the list of students
export const listOfStudents = [student1, student2, student3, student4, student5];
export default [student1, student2, student3, student4, student5];
