// # 3. Given a non-negative int n,
// # return the sum of its digits recursively (no loops).
// # Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
// # while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

function sumDigits (number) {
  if (typeof number === 'number' && number % number === 0 && number > 0) {
    if (number < 10) {
      return number
    } else {
      return (number % 10) + sumDigits(Math.floor(number / 10))
    }
  } else {
    return ('Please insert a number which is not negative and higher than zero.')
  }
}
console.log(sumDigits(123))
