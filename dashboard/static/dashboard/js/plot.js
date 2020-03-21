// var data = [
//   {
//     x: ['2013-10-04 22:23:00', '2013-11-04 22:23:00', '2013-12-04 22:23:00'],
//     y: [1, 3, 6],
//     type: 'scatter'
//   }
// ];

// Plotly.newPlot('potato-plot', data);



$( document ).ready(function() {

	setCSRF();

	setPotatoChart();
	setOnionChart();
	

	
});


// type: 1(-30+30)
// type: 2(1 year)
// type: 3(all)
function setPotatoChart(){
	plotPotato(type=1, "potato-plot_1", "potato", "Recent 30 days potato price");
	plotPotato(type=2, "potato-plot_2", "potato", "Last 1 year potato price");
	plotPotato(type=3, "potato-plot_3", "potato", "Full potato price");
}

function setOnionChart(){
	plotPotato(type=1, "onion-plot_1", "onion", "Recent 30 days onion price");
	plotPotato(type=2, "onion-plot_2", "onion", "Last 1 year onion price");
	plotPotato(type=3, "onion-plot_3", "onion", "Full onion price");
}


function plotPotato(type=1, id, item, title){
	var data_to_send = {
		item: item,
		type: type
	};

	requestPostData("/dashboard/getPrice", {data: data_to_send})
		.then(data=>{
			console.log(data)
			x = data["date"];
			y = data["price"];
			plotTimeSeries(id, x, y, type, item, title);

		})
}



function plotTimeSeries(id, x, y, type, item, title){

	var data = {}

	if(type == 1){


		data = [
			{
				x:x[0],
				y:y[0],
				type: 'scatter',
				name: item + ' price past'
			},
			{
				x:x[1],
				y:y[1],
				type: 'dashed',
				name: item + ' price predicted',
				mode: 'lines',
				line: {
					dash: 'dot',
					width: 4,
					color: "yellow"
				}

			},

		]

	}else{

		data = [
			{
	    		x,
	    		y,
	    		type: 'scatter',
	    		name: item + " price" 
  			}
	];

	}


	

	// mean_price = d3.mean(y);
	// console.log(mean_price)

	var layout = {
		width: '1000px',
		height: '500px',
		title: title, 
		showlegend: true,
		automargin: true,
		xaxis: {
			title: {
				text: "Date",
			},
			fixedrange: true,
		},
		yaxis: {
			title: {
				text: "Price in ₹ per 100 kg",
			},
			fixedrange: true,
		},
	};


	var config = {
		displayModeBar: false
	};

	plt = Plotly.newPlot(id, data, layout, config);
	console.log(plt)
}

function requestPostData(url, data) {
	data = {
		...data,
		_token:csrf_token
	}

	return new Promise((resolve, reject) => {
		$.ajax({
			url: url,
			type: 'POST',
			async: false,

			contentType: 'application/json',
			data: JSON.stringify(data),
			dataType: "json",
			processData: false,

			success: function(data, textStatus, jQxhr){
				var data = data["data"]
				resolve(data)
				
			},
			error: function(jqXhr, textStatus, errorThrown){
				console.log(errorThrown)
				reject(errorThrown)
			},
		});
	})
}

function setCSRF(){
	csrf_token = $("input[name=csrfmiddlewaretoken]").val();
	$("body").bind("ajaxSend", function(elm, xhr, s){
   		if (s.type == "POST") {
      		xhr.setRequestHeader('X-CSRF-Token', csrf_token);
   		}
	});
}