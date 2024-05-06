export default function createReportObject(employeesList) {
  // Create an object containing the allEmployees property and the getNumberOfDepartments method
  const report = {
    allEmployees: employeesList,
    getNumberOfDepartments() {
      return Object.keys(this.allEmployees).length;
    },
  };

  // Return the report object
  return report;
}
