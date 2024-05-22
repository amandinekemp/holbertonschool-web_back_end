export default function getStudentIdsSum(list) {
  // Reduce the table to the sum of all student IDs
  return list.reduce((accumulator, student) => accumulator + student.id, 0);
}
