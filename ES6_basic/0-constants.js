/**
* Returns a string declared with 'const'.
*/
export function taskFirst() {
  const task = 'I prefer const when I can.'
  return task
}

/**
* Returns a static string.
*/
export function getLast() {
  return ' is okay'
}

/**
* Returns a string declared with 'let'.
*/
export function taskNext() {
  let combination = 'But sometimes let'
  combination += getLast()

  return combination
}
