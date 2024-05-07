import ClassRoom from './0-classroom.js';

export default function initializeRooms() {
  // Array of classroom sizes
  const roomSizes = [19, 20, 34];
  // Empty array to store classrooms
  const classRooms = [];

  // Loop over classroom sizes
  for (const size of roomSizes) {
    // Create a new classroom with the current size
    const classroom = new ClassRoom(size);
    // Add the classroom to the array
    classRooms.push(classroom);
  }

  return classRooms;
}
