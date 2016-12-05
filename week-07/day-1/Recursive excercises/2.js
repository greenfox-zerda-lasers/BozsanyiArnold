// # 2. write a recursive function
// # that takes one parameter: n
// # and adds numbers from 1 to n

function countUp (n) {
  if (n !== 1) {
    return n + countUp(n - 1)
  } else {
    return 1
  }
}
console.log(countUp(10))
