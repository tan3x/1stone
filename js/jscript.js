console.log('Test Script' + "<br/>");

for(i=0; i<10; i++){
	console.log(i);
}

 var day = new Date();
     var today = day.getDay();
     var weekday = new Array(7);

	weekday[0]="Sunday";
	weekday[1]="Monday";
	weekday[2]="Tuesday";
	weekday[3]="Wednesday";
	weekday[4]="Thursday";
	weekday[5]="Friday";
    weekday[6]="Saturday";
    
    document.write("Today is"+"weekday[today]") ;

