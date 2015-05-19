<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap-theme.min.css">
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
  <style>
      html, body, #map-canvas {
       height: 100%;
       margin: 0px;
       padding: 0px;
      }
    </style>
  <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <link rel="icon" type="image/png" href="/static/findit-ico.png">
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Mapa</title>
    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&signed_in=true"></script>
    <script>
function initialize() {
var ubicaciones = {{ubicaciones}};
var myLatlng = new google.maps.LatLng(ubicaciones[0][0],ubicaciones[0][1]);
  var mapOptions = {
    zoom: 6,
    center: myLatlng
  }
  var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

  var marker, i;

    for (i = 0; i < ubicaciones.length; i++) {  
      marker = new google.maps.Marker({
        position: new google.maps.LatLng(ubicaciones[i][0], ubicaciones[i][1]),
        map: map
      });
      var infowindow = new google.maps.InfoWindow({
		    content: "<img src='"+{{imagen}}+"' style='float:left; padding: 5px;' /><strong>"+{{nombre}}+"</strong>: "+{{tuit}}
		    });
		    
      google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
          // infowindow.setContent(locations[i][0]);
          infowindow.open(map, marker);
        }
      })(marker, i));
}
}
google.maps.event.addDomListener(window, 'load', initialize);

    </script>
  </head>
  <body>
    	<div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
	     <div class="container">
	     	  <div class="navbar-header">
		       
		  </div>
		  <div class="navbar-collapse navbar-responsive-collapse collapse">
		       	<ul class="nav navbar-nav pull-right">
		       	   <li><a href="/" title="Busca un objeto en Twitter">Findit</a></li>
			 </ul>
		  </div>
	     </div>
	</div>
	<div id="map-canvas">
	</div>
  </body>
</html>
