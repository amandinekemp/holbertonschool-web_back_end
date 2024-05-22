// Updates the value of unique items in a Map to 100
export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }
  for (const [key, value] of map) {
    if (value === 1) {
      map.set(key, 100);
    }
  }
  return map;
}
