
		var a = [];
		a[0] = true;
		var numero = 5;     
		for (var i = 1; i < numero; i++) {
		  a.push(false);
		}
			

		document.getElementById("cat0").addEventListener("click", switch_cat0);

		document.getElementById("cat1").addEventListener("click", switch_cat1);
		document.getElementById("cat2").addEventListener("click", switch_cat2);
		document.getElementById("cat3").addEventListener("click", switch_cat3);
		document.getElementById("cat4").addEventListener("click", switch_cat4);

		function switch_cat0(){
			// var element = document.getElementById("cat0");
			console.log(a)
			// if n (!= a.find(true)){
			// 	console.log("alert")
			// 	element.classList.toggle("cat_text_white");
			// }   	
			// if (a.indexOf(true) != 0){
			// 	console.log("alert")
			// }		
			if(a[0] == true){
				console.log('removed')
				// document.getElementById("cat0").style.removeProperty('backgroundColor');
				document.getElementById("cat0").style.removeProperty('background-color')
				document.getElementById("cat0").style.removeProperty('borderRadius');

			}
		}
		function switch_cat1(){
			var element = document.getElementById("cattext1");
			console.log(1)
			if (a.indexOf(true) != 1){
				console.log("alert")
				

			}	
			 			
		}
		function switch_cat2(){
			var element = document.getElementById("cat2");
			console.log(2)
			if (a.indexOf(true) != 2){
				console.log("alert")
			}	
						
		}
		function switch_cat3(){
			var element = document.getElementById("cat3");
			console.log(3)
			if (a.indexOf(true) != 3){
				console.log("alert")
			}	
						
		}
		function switch_cat4(){
			var element = document.getElementById("cat4");
			console.log(4)
			if (a.indexOf(true) != 4){
				console.log("alert")
			}				
		}
