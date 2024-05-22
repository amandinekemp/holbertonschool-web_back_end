export default function updateStudentGradeByCity(list, city, newGrades) {
  // Filter the array to keep only students in the given city
  return list
    .filter((student) => student.location === city)
    // Create a new array with the students in the given city and their updated grades
    .map((student) => {
      // Find the student's new grade in the newGrades array
      const grade = newGrades.find((item) => item.studentId === student.id);
      // Return a new student object with the updated grade
      return { ...student, grade: grade ? grade.grade : 'N/A' };
    });
}
