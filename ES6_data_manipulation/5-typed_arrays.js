export default function createInt8TypedArray(length, position, value) {
  // Check if the position is outside the range of the buffer
  if (position >= length) {
    throw new Error('Position outside range');
  }

  // Create a new ArrayBuffer with the specified length
  const buffer = new ArrayBuffer(length);

  // Create a new DataView that allows us to manipulate the data in the buffer
  const view = new DataView(buffer);

  // Use the DataView to set the value of an 8-bit integer at the specified position
  view.setInt8(position, value);

  // Return the DataView so that we can continue to manipulate the data in the buffer if needed
  return view;
}
