% include('header.tpl')
<div class="jumbotron">
  <div class="container">
    <p>Busca un elemento:</p>
    <form action="/map" method="post">
      <p><input name="objeto" size="50" maxlength="500" type="text" required placeholder="Objeto a buscar: #Hashtag, @username, texto..." autofocus/></p>
      <p><input name="latitud" size="10" maxlength="15" type="text"/></p>
      <p><input name="longitud" size="10" maxlength="15" type="text"/></p>
      <p><input name="radio" size="10" maxlength="15" type="text"/></p>
      <p><input type="submit" class="button" value="Enviar" /></p>
      <script src="static/js/vendor/bootstrap.min.js"></script>
    </form>
  </div>  
</div>
</body>
</html>
