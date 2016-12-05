// # 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

function xRemover (string) {
  if (string.length === 0) {
    return string
  } else if (string[0].toLowerCase() === 'x') {
    return xRemover(string.slice(1, string.length))
  }else {
    return string[0] + xRemover(string.slice(1, string.length))
  }
}
console.log(xRemover('Xuxule'))
