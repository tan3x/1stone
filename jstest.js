<!DOCTYPE html>
<html>
<head>
	<title>JStest</title>
</head>
	<script type="text/javascript"> 

	alert("this is a JStest")

	var x= 1, y= 2, z= 3;
	var sum = x+y, min=x-y, multi=x*y, div= x/y ;
	var countries = ["Germany", "France", "Spain", "Italy"];

	document.write("Number of countries: " + countries.length + "<br/>" );

	

	countries.sort() ;
	

		for (i=0; i< countries.length ; i++)
		{
			document.write(countries[i] + "<br/>" + "<br/>"); 
		}



	// countries.prototype.displayItems = function() {
	// countries.displayItems();

	document.write("First No: = " + x + "<br />Second No: = " + y + " <br />");

	document.write(x + " + " + y + " = " + sum + "<br/>");

	document.write(x + " - " + y + " = " + min + "<br/>");

	document.write(x + " * " + y + " = " + multi + "<br/>");

	document.write(x + " / " + y + " = " + div + "<br/>");


	

</script>

	<body>

	

</body>
</html>
