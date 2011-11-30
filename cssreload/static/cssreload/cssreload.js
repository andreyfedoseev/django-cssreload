function django_cssreload(STATIC_URL, view) {
  if (!STATIC_URL.match(/^https?:\/\//)) {
    STATIC_URL = window.location.protocol + "//" + window.location.host + STATIC_URL;
  }
  var stylesheets = {};
  var links = document.getElementsByTagName("link");
  for (var i = 0; i < links.length; i++) {
    var link = links[i];
    if (link.rel && link.rel.toLowerCase() === "stylesheet" &&
        link.href && link.href.indexOf(STATIC_URL) == 0 &&
        link.href.indexOf(STATIC_URL + "cssreload/cssreload.css") == -1) {
      var path = link.href.slice(STATIC_URL.length);
      stylesheets[path] = [link, link.href, null];
    }
  }

  var widget = document.getElementById("django-cssreload");
  var enabled = widget.className === "enabled";

  function isEmpty(map) {
    for(var key in map) {
      if (map.hasOwnProperty(key)) {
        return false;
      }
    }
    return true;
  }

  function poll() {
    if (!enabled) {
      return;
    }
    if (isEmpty(stylesheets)) {
      return;
    }
    var data = "";
    for (var path in stylesheets) {
      if (data.length) {
        data += "&";
      }
      data = data + "s=" + encodeURIComponent(path);
    }
    var request = new XMLHttpRequest();
    request.open("POST", view, true);
    request.onreadystatechange = function() {
      if (request.readyState == 4 && request.status == 200) {
        var response = JSON.parse(request.responseText);
        for (var path in response) {
          var mtime = response[path];
          var stylesheet = stylesheets[path];
          if (mtime != stylesheet[2]) {
            stylesheet[2] = mtime;
            stylesheet[0].href = stylesheet[1] + "?reload=" + mtime;
          }
        }
      }
    }
    request.send(data);
    setTimeout(poll, 1000);
  }

  var buttons = widget.getElementsByTagName("a");

  // Disable button
  buttons[0].onclick = function() {
    enabled = false;
    widget.className = "";
    return false;
  }

  // Enable button
  buttons[1].onclick = function() {
    enabled = true;
    widget.className = "enabled";
    poll();
    return false;
  }
}
