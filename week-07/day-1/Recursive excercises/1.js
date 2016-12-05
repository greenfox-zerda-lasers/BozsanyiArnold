
// # 1. write a recursive function
// # that takes one parameter: n
// # and counts down from n

function countDown (n) {
  console.log(n)
  if (n !== 1) {
    return countDown(n - 1)
  } else {
    return n
  }
}
console.log(countDown(15))
