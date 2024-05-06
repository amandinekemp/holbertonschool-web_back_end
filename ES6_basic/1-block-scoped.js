// Exports a default function that takes a Boolean argument

export default function taskBlock(trueOrFalse) {
    let task = false
    let task2 = true

    if (trueOrFalse) {
      let task = true
      let task2 = false
    }

    return [task, task2]
  }
