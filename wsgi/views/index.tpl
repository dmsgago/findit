% include('header.tpl')
<section class="promo">
            <div class="wrap">
                <div class="promo-text">
                    <div class="promo-title">CREATIVITY LANDING PAGE</div>
                    <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</p>
                    <p>
			<a class="promo-button" href="{{authorize_url}}">Iniciar sesi&oacute;n</a>
		    </p>
                </div><!-- promo-text -->
                <img src="upload/promo.png" width="333" height="551" alt="">
            </div><!-- wrap -->
        </section><!-- promo -->
        <footer>
            <div class="wrap">
                <div class="logo">
                    <a href="#">
                        <img src="upload/logo-min.png" width="64" height="52" alt="SPORTHERE, YOUR SPORT DASHBOARD">
                    </a>
                </div><!-- logo -->
                <div class="istore"><a href="#">Available in Apple Store</a></div>
                <div class="copy">
                    <p>Copyright &copy; 2014 <a href="#">Сreativity</a></p>
                </div><!-- copy -->
                <div class="social">
                    <ul class="clearfix">
                        <li><a class="social-facebook" href="#" title="facebook">facebook</a></li>
                        <li><a class="social-twitter" href="#" title="twitter">twitter</a></li>
                        <li><a class="social-googleplus" href="#" title="google plus">google plus</a></li>
                    </ul>
                </div><!--social -->
            </div><!-- wrap -->
        </footer>
    </section><!-- main -->
    <script src="js/jquery.js"></script>
    <script src="js/library.js"></script>
    <script src="js/script.js"></script>
    <script src="js/retina.js"></script>
</body>
</html>
<a href="{{authorize_url}}">
       	    <img src="/static/images/login.png" onmouseover="this.src='/static/images/login2.png';" onmouseout="this.src='/static/images/login.png';"/>
