 var Ajax = function () {

   this.getData = function (cb) {
     var xhr = new XMLHttpRequest()
     xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos')
     xhr.send()
     xhr.onreadystatechange = function () {
       if (xhr.readyState === XMLHttpRequest.DONE) {
         cb(JSON.parse(xhr.response))
       }
     }
   }

   this.pushData = function (data) {
     var xhr = new XMLHttpRequest()
     xhr.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos')
     xhr.setRequestHeader('Content-Type', 'application/json')
     xhr.send(JSON.stringify({text: data}))
   }

   this.deleteDataFromApi = function (event) {
     var xhr = new XMLHttpRequest()
     xhr.open('DELETE', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + event.target.parentElement.id)
     xhr.send()
   }

   this.updateData = function (event) {
     var xhr = new XMLHttpRequest()
     xhr.open('PUT', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + event.target.parentElement.id)
     xhr.setRequestHeader('Content-Type', 'application/json')
     var textInTarget = event.target.parentElement.parentElement.getElementsByTagName('p')[0].innerText
     if (event.target.parentElement.parentElement.getAttribute('class') === 'done') {
       event.target.completed = false
       xhr.send(JSON.stringify({text: textInTarget, completed: false}))
     } else if (event.target.parentElement.parentElement.getAttribute('class') === 'undone') {
       event.target.completed = true
       xhr.send(JSON.stringify({text: textInTarget, completed: true}))
     }

    xhr.onreadystatechange = function () {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        console.log(xhr.response)
      }
    }
   }
 }

function App () {
  var barmi = this
  this.init = function () {
    this.ajax = new Ajax()
    this.ajax.getData(this.render.bind(this))
    this.addItem()
  }

  this.looper = function () {
    this.ajax.getData(this.render.bind(this))
  }.bind(this)

  this.render = function (items) {
    items.reverse()
    document.querySelector('ul').innerHTML = ''
    items.forEach(function (e) {
      var listElement = document.createElement('li')
      if (e.completed === true) {
        listElement.setAttribute('class', 'done')
      } else {
        listElement.setAttribute('class', 'undone')
      }
      listElement.innerHTML = '<p>' + e.text + '</p><div class="inlinecontrol" id="' + e.id + '"><button></button><div class="checkbox"></div></div>'
      document.querySelector('ul').appendChild(listElement)
    })
    this.deleting()
    this.setState()
  }


  this.addItem = function () {
    document.querySelector('button').addEventListener('click', function (e) {
      this.ajax.pushData(this.data())
    }.bind(this))
  }

  this.deleting = function () {
    document.querySelectorAll('.inlinecontrol button').forEach(function (e) {
      e.addEventListener('click', function (e) {
        this.ajax.deleteDataFromApi(e)
        if (e.target.parentElement.parentElement.getAttribute('class') === 'done') {
          e.target.parentElement.parentElement.setAttribute('class', 'done deleted')
        }else {
          e.target.parentElement.parentElement.setAttribute('class', 'undone deleted')
        }
      }.bind(this))

    }.bind(this))
  }

  this.setState = function () {
    document.querySelectorAll('.checkbox').forEach(function (e) {
      e.addEventListener('click', function (e) {
        this.ajax.updateData(e)
        console.log(this)
        if (e.target.parentElement.parentElement.getAttribute('class') === 'undone') {
          e.target.parentElement.parentElement.setAttribute('class', 'done')
        } else {
          e.target.parentElement.parentElement.setAttribute('class', 'undone')
        }
      }.bind(this))

    }.bind(this))
  }

  this.data = function () {
    var input = document.querySelector('input')
    return input.value
  }
}

var app = new App()

app.init()

setInterval(app.looper, 500)
