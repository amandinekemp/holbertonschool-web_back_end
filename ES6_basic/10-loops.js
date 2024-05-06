export default function appendToEachArrayValue(array, appendString) {
  // New array to store modified values
  const newArray = [];

  // Loop over each value in original array
  for (const value of array) {
    // Concatenate the string to the current value and add the result to the new array
    newArray.push(appendString + value);
  }

  // Return the modified array
  return newArray;
}
