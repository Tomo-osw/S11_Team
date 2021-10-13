var map;

function initialize() {
  var latlng = new google.maps.LatLng(35.680865,139.767036);
  var opts = {
    zoom: 13,
    center: latlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  map = new google.maps.Map(document.getElementById("map_canvas"), opts);
}

function toTokyo() {
  map.panTo(new google.maps.LatLng(35.680865,139.767036));
}

function toShinbashi() {
  map.panTo(new google.maps.LatLng(35.666397,139.758153));
}

function toShinagawa() {
  map.panTo(new google.maps.LatLng(35.629867,139.74015));
}