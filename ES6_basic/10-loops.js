// Adds a string to each value in an array
export default function appendToEachArrayValue(array, appendString) {
  // Loop over each element in the array
  for (let idx = 0; idx < array.length; idx++) {
    // Concatenate the string to the current value
    array[idx] = appendString + array[idx];
  }

  // Return the modified array
  return array;
}
