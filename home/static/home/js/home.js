jQuery(document).ready(function($) {
	$(".dropdown-trigger").dropdown();
    $('select').formSelect();
    // drawchart();

    plotChartParent();

});


function plotChartParent(){
	commodity_name = "Onion";
	mandi_name = "LASALGAON";
	state_name = "MAHARASHTRA";

	data = {
		commodity_name,
		mandi_name,
		state_name
	}
	chart_id = ["chart11", "chart12" ,"chart13"]

	plotChart(data, chart_id)



	mandi_name = "BANGALORE";
	state_name = "KARNATAKA";

	data = {
		commodity_name,
		mandi_name,
		state_name
	}
	chart_id = ["chart21", "chart22" ,"chart23"]

	plotChart(data, chart_id)


	mandi_name = "AZADPUR";
	state_name = "NCT OF DELHI";

	data = {
		commodity_name,
		mandi_name,
		state_name
	}
	chart_id = ["chart31", "chart32" ,"chart33"]

	plotChart(data, chart_id)





}

function plotChart(data, chart_id){
	

	requestPostData("/home/get_mandi_data_1_year", {"data": data})
	.then(data=>{
		console.log(data);
		date = data["date"];
		// date = date.map(Date)

		mandi_price = data["mandi_price"]
		mandi_avg = data["mandi_avg"]
		mandi_std =  data["mandi_std"]

		plotChart1(chart_id[0], date, mandi_price, mandi_avg,mandi_std, "Mandi Price");

		retail_price = data["retail_price"]
		retail_avg = data["retail_avg"]
		retail_std =  data["retail_std"]

		plotChart1(chart_id[1], date, retail_price, retail_avg,retail_std, "Retail Price");

		arrival = data["arrival"]
		arrival_avg = data["arrival_avg"]
		arrival_std =  data["arrival_std"]

		plotChart1(chart_id[2], date, arrival, arrival_avg,arrival_std, "Arrival");

	})
}


function plotChart1(chart_id, date, value, avg, std, data_label){
	var ctx = document.getElementById(chart_id).getContext('2d');


	mean_plus_std = avg.map(function (num, idx) {
  		return num + std[idx];
	});

	mean_minus_std = avg.map(function (num, idx) {
  		return num - std[idx];
	});


	price = value;
	mean = avg;

	s1 = {
		label: data_label,
		borderColor: "green",
		data: price,
		fill: false,
		pointRadius: 0,
		// borderWidth: 1,
	}

	s2 = {
		label: "Avg",
		borderColor: "grey",
		data: mean,
		borderDash: [5,5],
		// borderWidth: 1,
		fill: false,
		pointRadius: 0,
	}

	s3 = {
		data: mean_minus_std,
		pointRadius: 0,
		fill: '+1',
		// fillBetweenSet: 1,
		// strokeColor: "rgba(255,0,0, 0.2)",
		// fillColor: "rgba(255,0,0, 0.2)"
	}

	s4 = {
		data: mean_plus_std,
		pointRadius: 0,
		fill: false,
	}

	


	var myChart = new Chart( ctx, {
		type: 'line',
		data: {
			labels: date,
			datasets: [s1, s2, s3, s4],
		},
		options: {
	        scales: {
	            xAxes: [{
	                type: 'time',
	                time: {
	                	parser: 'YYYY-MM-DD',
	                    unit: 'day',
	                    day: 'MMM YY',
	                    displayFormats:{
	                    	day: 'MMM YY'
	                    }
	                },
	                ticks: {
	                	// max: 5,
	                	// step: 60,
	                	autoSkip: true,
        				maxTicksLimit: 12
	                }
	            }]
	        },
	        tooltips: {
            	mode: 'point'
        	},
        	legend: {
           labels: {
               filter: function(legendItem, chartData) {
                if (legendItem.datasetIndex >= 2) {
                  return false;
                }
               return true;
               }
            }
        }

	    }
	});


}



function drawchart() {
	var ctx = document.getElementById('chart11').getContext('2d');
	var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

}