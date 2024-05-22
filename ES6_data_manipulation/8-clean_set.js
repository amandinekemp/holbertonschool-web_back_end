export default function cleanSet(set, startString) {
  // Initialize an empty array to store the cleaned strings
  const string = [];

  // Check if the input arguments are valid
  if (
    typeof set !== 'object' // Check if set is an object
    || typeof startString !== 'string' // Check if startString is a string
    || startString.length === 0 // Check if startString is not an empty string
  ) {
    // If the input is invalid, return an empty string
    return '';
  }

  // Iterate over each item in the set
  for (const item of set) {
    // Check if the item is not null or undefined and starts with the startString
    if (item && item.startsWith(startString)) {
      // If it does, add the cleaned string to the array
      string.push(item.slice(startString.length));
    }
  }

  // Join the cleaned strings with a hyphen and return the result
  return string.join('-');
}
