from browser import document
from browser import window

def details(event):
  element = event.target
  element.href = element.name + ".html"
  window.open(element.href)

document["h"].bind("click", details)
document["he"].bind("click", details)
document["li"].bind("click", details)
document["be"].bind("click", details)
document["b"].bind("click", details)
document["c"].bind("click", details)
document["n"].bind("click", details)