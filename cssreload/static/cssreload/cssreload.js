function django_cssreload(STATIC_URL, view) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }



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
      request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
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
