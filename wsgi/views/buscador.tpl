% include('header.tpl')
				<li><a href="/" title="Busca un objeto en Twitter">Findit</a></li>
			</ul>
		</div>
	</div>
</div>
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
    </form>
  </div>  
</div>
</body>
</html>
