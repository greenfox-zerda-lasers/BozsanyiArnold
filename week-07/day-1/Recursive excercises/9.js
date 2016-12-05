// # 9. Given a string, compute recursively a new string where all the
// # adjacent chars are now separated by a "*".

function starFiller (string) {
  if (string.length === 1) {
    return string
  } else {
    return string[0] + '*' + starFiller(string.slice(1, string.length))
  }
}
console.log(starFiller('Xuxule'))
