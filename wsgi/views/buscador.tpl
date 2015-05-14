% include('header.tpl')
<div class="jumbotron">
  <div class="container">
  <form action="/map" method="post">
    <p>
    	     Buscar por hashtag:
    	     <input name="TipoBusqueda" id="ElegirHashtag"  value="0" type="radio"/>
	     <br/>
	     Buscar por usuario
    	     <input name="TipoBusqueda" id="ElegirUsuario" value="1" type="radio"/>
    </p>
      <p><input name="hashtag" size="20" maxlength="500" type="text" placeholder="#Hashtag" autofocus/></p>
      <p><input name="geoposs" size="20" maxlength="50" type="text" placeholder="Localizaci&oacute;n"/></p>
      <p><input name="username" size="20" maxlength="50" type="text" placeholder="username"/></p>
      <p><input name="username" size="20" maxlength="50" type="text" placeholder="N&uacute;mero de tuits"/></p>
      <p><input type="submit" class="button" value="Enviar" /></p>
      <!-- Bootstrap -->
      <script src="static/js/vendor/bootstrap.min.js"></script>
    </form>
  </div>  
</div>
</body>
</html>
