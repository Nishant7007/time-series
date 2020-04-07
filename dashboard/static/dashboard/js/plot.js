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
	//mandi
	plotChart(type=1, id="plot_mandi_potato_lucknow_1", item="potato", mandi="lucknow", source="mandi",  title="Recent 30 days potato price", 185, 2500);
	plotChart(type=1, id="plot_mandi_potato_kolkata_1", item="potato", mandi="kolkata", source="mandi",  title="Recent 30 days potato price", 185, 2500);

	plotChart(type=2, id="plot_mandi_potato_lucknow_2", item="potato", mandi="lucknow", source="mandi",  title="Last 1 year potato price", 185, 2500);
	plotChart(type=2, id="plot_mandi_potato_kolkata_2", item="potato", mandi="kolkata", source="mandi",  title="Last 1 year potato price", 185, 2500);

	plotChart(type=3, id="plot_mandi_potato_lucknow_3", item="potato", mandi="lucknow", source="mandi",  title="Full potato price", 185, 2500);
	plotChart(type=3, id="plot_mandi_potato_kolkata_3", item="potato", mandi="kolkata", source="mandi",  title="Full potato price", 185, 2500);

	//retail
	plotChart(type=1, id="plot_retail_potato_lucknow_1", item="potato", mandi="lucknow", source="retail",  title="Recent 30 days potato price", 400, 3100);
	plotChart(type=1, id="plot_retail_potato_kolkata_1", item="potato", mandi="kolkata", source="retail",  title="Recent 30 days potato price", 400, 3100);

	plotChart(type=2, id="plot_retail_potato_lucknow_2", item="potato", mandi="lucknow", source="retail",  title="Last 1 year potato price", 400, 3100);
	plotChart(type=2, id="plot_retail_potato_kolkata_2", item="potato", mandi="kolkata", source="retail",  title="Last 1 year potato price", 400, 3100);

	plotChart(type=3, id="plot_retail_potato_lucknow_3", item="potato", mandi="lucknow", source="retail",  title="Full potato price", 400, 3100);
	plotChart(type=3, id="plot_retail_potato_kolkata_3", item="potato", mandi="kolkata", source="retail",  title="Full potato price", 400, 3100);


	//arrival
	// plotChart(type=1, id="plot_arrival_potato_lucknow_1", item="potato", mandi="lucknow", source="arrival",  title="Recent 30 days potato arrival", 0, 1007);
	// plotChart(type=1, id="plot_arrival_potato_kolkata_1", item="potato", mandi="kolkata", source="arrival",  title="Recent 30 days potato arrival", 0, 1007);

	// plotChart(type=2, id="plot_arrival_potato_lucknow_2", item="potato", mandi="lucknow", source="arrival",  title="Last 1 year potato arrival", 0, 1007);
	// plotChart(type=2, id="plot_arrival_potato_kolkata_2", item="potato", mandi="kolkata", source="arrival",  title="Last 1 year potato arrival", 0, 1007);

	// plotChart(type=3, id="plot_arrival_potato_lucknow_3", item="potato", mandi="lucknow", source="arrival",  title="Full potato arrival", 0, 1007);
	// plotChart(type=3, id="plot_arrival_potato_kolkata_3", item="potato", mandi="kolkata", source="arrival",  title="Full potato arrival", 0, 1007);

}

function setOnionChart(){
	// mandi
	plotChart(type=1, id="plot_mandi_onion_mumbai_1", item="onion", mandi="mumbai", source="mandi",  title="Recent 30 days onion price", min_y=101, max_y=12000);
	plotChart(type=1, id="plot_mandi_onion_bangalore_1", item="onion", mandi="bangalore", source="mandi",  title="Recent 30 days onion price", min_y=101, max_y=12000);
	plotChart(type=1, id="plot_mandi_onion_delhi_1", item="onion", mandi="delhi", source="mandi",  title="Recent 30 days onion price", min_y=101, max_y=12000);

	plotChart(type=2, id="plot_mandi_onion_mumbai_2", item="onion", mandi="mumbai", source="mandi",  title="Last 1 year onion price", min_y=101, max_y=12000);
	plotChart(type=2, id="plot_mandi_onion_bangalore_2", item="onion", mandi="bangalore", source="mandi",  title="Last 1 year onion price", min_y=101, max_y=12000);
	plotChart(type=2, id="plot_mandi_onion_delhi_2", item="onion", mandi="delhi", source="mandi",  title="Last 1 year onion price", min_y=101, max_y=12000);

	plotChart(type=3, id="plot_mandi_onion_mumbai_3", item="onion", mandi="mumbai", source="mandi",  title="Full onion price", min_y=101, max_y=12000);
	plotChart(type=3, id="plot_mandi_onion_bangalore_3", item="onion", mandi="bangalore", source="mandi",  title="Full onion price", min_y=101, max_y=12000);
	plotChart(type=3, id="plot_mandi_onion_delhi_3", item="onion", mandi="delhi", source="mandi",  title="Full onion price", min_y=101, max_y=12000);

	//retail
	plotChart(type=1, id="plot_retail_onion_mumbai_1", item="onion", mandi="mumbai", source="retail",  title="Recent 30 days onion price", 400, 15000);
	plotChart(type=1, id="plot_retail_onion_bangalore_1", item="onion", mandi="bangalore", source="retail",  title="Recent 30 days onion price", 400, 15000);
	plotChart(type=1, id="plot_retail_onion_delhi_1", item="onion", mandi="delhi", source="retail",  title="Recent 30 days onion price", 400, 15000);

	plotChart(type=2, id="plot_retail_onion_mumbai_2", item="onion", mandi="mumbai", source="retail",  title="Last 1 year onion price", 400, 15000);
	plotChart(type=2, id="plot_retail_onion_bangalore_2", item="onion", mandi="bangalore", source="retail",  title="Last 1 year onion price", 400, 15000);
	plotChart(type=2, id="plot_retail_onion_delhi_2", item="onion", mandi="delhi", source="retail",  title="Last 1 year onion price", 400, 15000);

	plotChart(type=3, id="plot_retail_onion_mumbai_3", item="onion", mandi="mumbai", source="retail",  title="Full onion price", 400, 15000);
	plotChart(type=3, id="plot_retail_onion_bangalore_3", item="onion", mandi="bangalore", source="retail",  title="Full onion price", 400, 15000);
	plotChart(type=3, id="plot_retail_onion_delhi_3", item="onion", mandi="delhi", source="retail",  title="Full onion price", 400, 15000);


	// arrival
	// plotChart(type=1, id="plot_arrival_onion_mumbai_1", item="onion", mandi="mumbai", source="arrival",  title="Recent 30 days onion arrival", 0, 25000);
	// plotChart(type=1, id="plot_arrival_onion_bangalore_1", item="onion", mandi="bangalore", source="arrival",  title="Recent 30 days onion arrival", 0, 25000);
	// plotChart(type=1, id="plot_arrival_onion_delhi_1", item="onion", mandi="delhi", source="arrival",  title="Recent 30 days onion arrival", 0, 25000);

	// plotChart(type=2, id="plot_arrival_onion_mumbai_2", item="onion", mandi="mumbai", source="arrival",  title="Last 1 year onion arrival", 0, 25000);
	// plotChart(type=2, id="plot_arrival_onion_bangalore_2", item="onion", mandi="bangalore", source="arrival",  title="Last 1 year onion arrival", 0, 25000);
	// plotChart(type=2, id="plot_arrival_onion_delhi_2", item="onion", mandi="delhi", source="arrival",  title="Last 1 year onion arrival", 0, 25000);

	// plotChart(type=3, id="plot_arrival_onion_mumbai_3", item="onion", mandi="mumbai", source="arrival",  title="Full onion arrival", 0, 25000);
	// plotChart(type=3, id="plot_arrival_onion_bangalore_3", item="onion", mandi="bangalore", source="arrival",  title="Full onion arrival", 0, 25000);
	// plotChart(type=3, id="plot_arrival_onion_delhi_3", item="onion", mandi="delhi", source="arrival",  title="Full onion arrival", 0, 25000);



}


function plotChart(type=1, id="", item="", mandi="", source="", title="", min_y, max_y){
	var data_to_send = {
		type,
		item,
		mandi,
		source,
	};

	requestPostData("/dashboard/getDashBoardData", {data: data_to_send})
		.then(data=>{
			console.log("data recieved")
			console.log(data)
			x = []
			y = []

			if(type==1){
				past = data["past"]
				pred = data["pred"]

				past_orig_x = past[0][0]
				past_orig_y = past[0][1]

				past_miss_x = past[1][0]
				past_miss_y = past[1][1]

				pred_x = pred[0]
				pred_y = pred[1]

				x.push(past_orig_x, past_miss_x, pred_x)
				y.push(past_orig_y, past_miss_y, pred_y)
			}
			else{
				orig = data["orig"]
				miss = data["miss"]

				orig_x = orig[0]
				orig_y = orig[1]

				miss_x = miss[0]
				miss_y = miss[1]

				x.push(orig_x, miss_x)
				y.push(orig_y, miss_y)

			}

			plotTimeSeries(id, x, y, type, item, title, source, min_y, max_y);

		})
}



function plotTimeSeries(id, x, y, type, item, title, source, min_y, max_y){
	y_title= "Price in ₹ per 100 kg";
	measure = "price";
	if(source == "arrival"){
		y_title = "Tonnes";
		measure = "arrival"
	}

	var data = {}

	if(type == 1){


		data = [
			{
				x:x[0],
				y:y[0],
				// mode: 'markers',
				type: 'scatter',
				mode: "lines+markers",
				line: {
    				// 'color': "red",
    				// 'dash': 'dash',
    			},
				name: `${item} ${measure} past original`,
				connectgaps: false
			},
			{
				x:x[1],
				y:y[1],
				type: 'scatter',
				// mode: "lines",
				// line:{
				// 	color: "red",
				// },
				mode: 'lines+markers',
    			line: {
    				'color': "red",
    				'dash': 'dot'
    			},
				name: `${item} ${measure} past missing`,
				connectgaps: false
			},
			{
				x:x[2],
				y:y[2],
				type: 'dashed',
				name: `${item} ${measure} predicted`,
				connectgaps: false,
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
				x:x[0],
				y:y[0],
				// mode: 'markers',
				type: 'scatter',
				mode: "lines",
				line: {
					width: 4,
				},

				name: `original`,
				connectgaps: false
			},
			{
				x:x[1],
				y:y[1],
				type: 'scatter',
				mode: "lines",
				line: {
					color: "red",
					width: 2,
				},
				// mode: 'lines+markers',
				// line:{
				// 	'color': 'red',
				// 	'dash': 'dot'
				// },
    			// marker: {
    			// 	'color': "red",
    			// },
				name:`missing`,
				connectgaps: false
			},
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
				text: y_title,
			},
			range: [min_y, max_y],
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