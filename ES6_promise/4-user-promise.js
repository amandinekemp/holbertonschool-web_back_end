// Promise-based user sign-up function
export default function signUpUser(firstName, lastName) {
  return Promise.resolve({ firstName, lastName });
}
