function dirReduc(arr) {
  let str = arr.join('')
  let pattern = /NORTHSOUTH|EASTWEST|SOUTHNORTH|WESTEAST/
  while (pattern.test(str)) {
    str = str.replace(pattern,'')
  }
  return str.match(/(NORTH|SOUTH|EAST|WEST)/g)||[]
}
