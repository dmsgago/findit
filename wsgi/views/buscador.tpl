% include('header.tpl')
<div class="jumbotron">
  <div class="container">
    <p>Busca por un elemento:</p>
    <input name="BuscarPorHashtag" id="ElegirHashtag" value="0" type="radio">
    <input name="BuscarPorUsuario" id="ElegirUsuario" value="1" type="radio">
    <form action="/map" method="post">
      <p><input name="hashtag" size="20" maxlength="500" type="text" required placeholder="Buscar por hashtag: #Hashtag" autofocus/></p>
      <p><input name="username" size="20" maxlength="50" type="text" placeholder="Buscar por usuario: @username"/></p>
      <p><input name="geoposs" size="20" maxlength="50" type="text" placeholder="Latitud,longitud,radio"/></p>
      <p><input type="submit" class="button" value="Enviar" /></p>
      <!-- Bootstrap -->
      <script src="static/js/vendor/bootstrap.min.js"></script>
    </form>
  </div>  
</div>
</body>
</html>
