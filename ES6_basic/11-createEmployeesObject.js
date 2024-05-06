export default function createEmployeesObject(departmentName, employees) {
  // Create an object with a property corresponding to the department name
  // and a value corresponding to the array of employees
  const obj = { [departmentName]: employees };

  // Return the created object
  return obj;
}
