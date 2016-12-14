// Adding elements

var input = document.querySelector('input');

var addButton = document.querySelector('button')

var theList = document.querySelector('ul');

var listElements = [];



function createListElement () {
  if (input.value.length > 0) {
    var element = document.createElement('li');

    var basicContent = '<p>'+ input.value +'</p><div class="inlinecontrol"><button type="button"></button><div class="checkbox"></div></div>';

    element.innerHTML = basicContent;

    listElements.push(element);

    document.querySelector('ul').appendChild(listElements[listElements.length - 1])
  } else {
    alert('Please put some content for your TODO item. :)')
  }
}

document.querySelector('button').addEventListener('click', createListElement);
