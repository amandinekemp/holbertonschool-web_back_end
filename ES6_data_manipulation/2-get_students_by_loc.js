// Returns students in a given city
export default function getStudentsByLocation(list, city) {
  return list.filter((student) => student.location === city);
}
