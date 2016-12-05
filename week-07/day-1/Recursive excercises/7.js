// # 7. Given a string, compute recursively (no loops) a new string where all the
// # lowercase 'x' chars have been changed to 'y' chars.

function changer (string) {
  if (string.length === 0) {
    return string
  } else if (string[0] === 'x') {
    return 'y' + changer(string.slice(1, string.length))
  } else {
    return string[0] + changer(string.slice(1, string.length))
  }
}
console.log(changer('xuxule'))
