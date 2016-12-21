// read Input

var ourData

function checkInput () {
  var input = document.querySelector('input')
  ourData = input.value
}

var theList = document.querySelector('ul')
var elementList

// AJAX functions :

function getData () {
  var xhr = new XMLHttpRequest()
  xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos')
  xhr.send()
  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE) {
        elementList = JSON.parse(xhr.response)
    }
  }
}

function pushData () {
  var xhr = new XMLHttpRequest()
  xhr.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos')
  xhr.setRequestHeader('Content-Type', 'application/json')
  if (ourData.length > 0){
    xhr.send(JSON.stringify({text: ourData}))
  }
}

function deleteData (id) {
  var xhr = new XMLHttpRequest()
  xhr.open('DELETE', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + (id))
  xhr.send()
}

function setData (data, boolean, id) {
  var xhr = new XMLHttpRequest()
  xhr.open('PUT', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + (id))
  xhr.send({text: data, completed: boolean})
}

function renderElements () {
  elementList.forEach(function (e) {
    var listElement = document.createElement('li')
    listElement.innerHTML = '<p>' + e.text + '</p><div class="inlinecontrol"><button type="button"></button><div class="checkbox"></div></div>'
    theList.appendChild(listElement)
  })
}

function addAnElement () {
  var listElement = document.createElement('li')
  listElement.innerHTML = '<p>' + elementList[elementList.length - 1].text + '</p><div class="inlinecontrol"><button type="button"></button><div class="checkbox"></div></div>'
  theList.appendChild(listElement)
}

function setItDone () {

}
