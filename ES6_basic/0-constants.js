/**
* Returns a string declared with 'const'.
* return {string} - A string.
*/
export function taskFirst() {
    const task = 'I prefer const when I can.'
    return task
  }

export function getLast() {
    return ' is okay'
  }

export function taskNext() {
    let combination = 'But sometimes let'
    combination += getLast()

    return combination
  }
