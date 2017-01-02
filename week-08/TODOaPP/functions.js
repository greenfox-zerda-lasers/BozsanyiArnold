 var Ajax = function () {

   this.getData = function (cb) {
     var xhr = new XMLHttpRequest()
     xhr.open('GET', 'http://localhost:3000/todos/')
     xhr.send()
     xhr.onreadystatechange = function () {
       if (xhr.readyState === XMLHttpRequest.DONE) {
         cb(JSON.parse(xhr.response))
       }
     }
   }

   this.pushData = function (data, cb) {
     var xhr = new XMLHttpRequest()
     xhr.open('POST', 'http://localhost:3000/todos/')
     xhr.setRequestHeader('Content-Type', 'application/json')
     xhr.send(JSON.stringify({text: data}))
     xhr.onreadystatechange = function () {
       if (xhr.readyState === XMLHttpRequest.DONE) {
         cb(JSON.parse(xhr.response))
       }
     }
   }

   this.deleteDataFromApi = function (event, cb) {
     var xhr = new XMLHttpRequest()
     xhr.open('DELETE', 'http://localhost:3000/todos/' + event.target.parentElement.id)
     xhr.send()
     xhr.onreadystatechange = function () {
       if (xhr.readyState === XMLHttpRequest.DONE) {
         cb(JSON.parse(xhr.response))
       }
     }
   }

   this.updateData = function (event, cb) {
     var xhr = new XMLHttpRequest()
     xhr.open('PUT', 'http://localhost:3000/todos/' + event.target.parentElement.id)
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

  this.render = function (items) {
    items.reverse()
    document.querySelector('ul').innerHTML = ''
    items.forEach(function (e) {
      var listElement = document.createElement('li')
      if (e.completed) {
        listElement.classList.add('done')
      } else {
        listElement.classList.add('undone')
      }
      listElement.innerHTML = '<p>' + e.text + '</p><div class="inlinecontrol" id="' + e.id + '"><button></button><div class="checkbox"></div></div>'
      document.querySelector('ul').appendChild(listElement)
    })
    this.deleting()
    this.setState()
  }


  this.addItem = function () {
    document.querySelector('button').addEventListener('click', function (e) {
      this.ajax.pushData(this.data(), function (){
        this.ajax.getData(this.render.bind(this))
      }.bind(this))
    }.bind(this))
  }

  this.deleting = function () {
    document.querySelectorAll('.inlinecontrol button').forEach(function (e) {
      e.addEventListener('click', function (e) {
        this.ajax.deleteDataFromApi(e, function (){
          this.ajax.getData(this.render.bind(this))
        }.bind(this))
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
        this.ajax.updateData(e, function (){
          this.ajax.getData(this.render.bind(this))
        }.bind(this))
        console.log(this)
        if (e.target.parentElement.parentElement.classList.contains('undone')) {
          e.target.parentElement.parentElement.classList.remove('undone')
          e.target.parentElement.parentElement.classList.add('done')
        } else {
          e.target.parentElement.parentElement.classList.remove('done')
          e.target.parentElement.parentElement.classList.add('undone')
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
