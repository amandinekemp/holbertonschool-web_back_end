export default function hasValuesFromArray(set, array) {
  // Iterate over each element of the array
  for (const element of array) {
    // Check if the element is present in the Set object
    if (!set.has(element)) {
      // If it's not present, immediately return false
      return false;
    }
  }
  // If all elements are present in the Set object, return true
  return true;
}
