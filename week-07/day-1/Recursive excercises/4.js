// # 4. Given base and n that are both 1 or more, compute recursively (no loops)
// # the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

function powerN (n, k) {
  if (k === 1) {
    return n
  } else {
    return n * powerN(n, k - 1)
  }
}
console.log(powerN(4, 5))
