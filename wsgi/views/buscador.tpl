% include('header.tpl')
<div class="jumbotron">
  <div class="container">
  <form action="/map" method="post">
      <p><input name="hashtag" size="20" maxlength="500" type="text" placeholder="#Hashtag" autofocus/></p>
      <p><input name="username" size="20" maxlength="50" type="text" placeholder="@username"/></p>
      <p><input type="submit" class="button" value="0" name="TipoBusqueda" /></p>
      <p><input type="submit" class="button" value="1" name="TipoBusqueda" /></p>

      <!-- Bootstrap -->
      <script src="static/js/vendor/bootstrap.min.js"></script>
    </form>
  </div>  
</div>
</body>
</html>
