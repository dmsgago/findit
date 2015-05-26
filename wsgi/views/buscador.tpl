% include('header.tpl')
<div class="jumbotron">
  <div class="container">
  <form action="/map" method="post">
     <div class="col-md-4">
      <p><input name="hashtag" size="20" maxlength="500" type="text" placeholder="#Hashtag" autofocus/></p>
      <p><button type="submit" class="button" value="0" name="TipoBusqueda" />Enviar</button></p>
     </div>
     <div class="col-md-4">
      <p><input name="username" size="20" maxlength="50" type="text" placeholder="@username"/></p>
      <p><button type="submit" class="button" value="1" name="TipoBusqueda" />Enviar</button></p>
     </div>
      <!-- Bootstrap -->
      <script src="static/js/vendor/bootstrap.min.js"></script>
    </form>
  </div>  
</div>
</body>
</html>
