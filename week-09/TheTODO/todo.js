var Ajax = function () {
  this.xhr = new XMLHttpRequest();
  this.url = 'http://localhost:3000/todos/';
  this.xhr.setRequestHeader('Content-Type', 'application/json');
};

Ajax.prototype.request = function (method, cb, data, id) {
  this.xhr.open(method, this.url + id);
  this.xhr.send(data);
  if (cb !== undefined) {
    this.xhr.onreadystatechange = function () {
      if (this.xhr.readyState === XMLHttpRequest.DONE) {
        cb(JSON.parse(this.xhr.response));
      }
    };
  }
};

Ajax.prototype.get = function (func) {
  this.request('GET', func, null, '');
};

var App = function () {
  this.init = function () {
    this.ajax = new Ajax();
    this.ajax.get(this.render);
  };
};

App.prototype.render = function (data)
