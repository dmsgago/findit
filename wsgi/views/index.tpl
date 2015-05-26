% include('header.tpl')
<div class="jumbotron">
  <div class="container">
    <script>
     function myFunction() {
     var myWindow = window.open("{{authorize_url}}", "MsgWindow", "width=650, height=450");
     }
   </script>
    <a href="#"><span onclick="myFunction()">Buscar Tuit</span></a>
  </div>
</div>
<!-- Bootstrap -->
<script src="static/js/vendor/bootstrap.min.js"></script>
</body>
</html>
