<h3><img class="alignnone size-full wp-image-53" src="https://getpython.files.wordpress.com/2019/04/flask_mvc.png" alt="flask_mvc.png" width="381" height="381" /></h3>
<h3><strong>What is MVC?</strong></h3>
The <b>Model-View-Controller (MVC)</b> is an architectural pattern that separates an application into three main logical components: the <b>model</b>, the view, and the controller. Each of these components is built to handle specific development aspects of an application. MVC is one of the most frequently used industry-standard web development frameworks` to create scalable and extensible projects.

Generally, Flask is actually not an MVC framework. It is a minimalistic framework which gives you a lot of freedom in how you structure your application, but MVC pattern is a very good fit for what Flask provides.
<h3><strong>MVC Sructure:</strong></h3>
<img class="alignnone size-full wp-image-54" src="https://getpython.files.wordpress.com/2019/04/base_mvc.png" alt="base_mvc" width="1024" height="403" />

This is how MVC app looks like , here flask_api is my app name , you can name it whatever you want , static folder contains our css files inside a css folder and images in images folder. Templates folder contains our html files whereas manage.py file contain host number to run app on particular local ip.

requirement.text file conatins packages information for installation.

<strong>MVC App folder layout:</strong>

<img class="alignnone size-full wp-image-55" src="https://getpython.files.wordpress.com/2019/04/main_mvc.png" alt="main_mvc" width="961" height="552" />

As we can see, this app folder have bunch of files, i will explain each file functionalaty and purpose one by one.
<ol>
	<li>__init__.py  this file use to initialise our  app's urls and model , you can chek it.</li>
	<li>models.py this file is use to store data in database using ORM (object relational management sructure ) write now its empty but  i  will discuss in my upcoming post.</li>
	<li>settings.py file contains general setting regarding static , templates folder path , secret_key amd database details.</li>
	<li>urls.py file contains unique url for each functions which we defined in our views.py app.</li>
	<li>views.py this is core file of this app , it can contains multiple function , here we just write small functions just for bind up urls with app.</li>
</ol>
<h2>How to run this app ?</h2>
<ul>
	<li style="list-style-type: none;">
<ul>
	<li>Install python by the following command</li>
	<li><code>sudo apt-get python3-pip</code></li>
</ul>
</li>
</ul>
<ul>
	<li style="list-style-type: none;">
<ul>
	<li>Install requirement.txt file  by the following command</li>
	<li><code>pip install -r requirements.txt</code></li>
</ul>
</li>
</ul>
<ol>
	<li>Now run the app on base dir where manage.py file is placed</li>
	<li>run this command here in your terminal <span style="text-decoration: underline;"><b>python3 manage.py</b> </span></li>
</ol>
