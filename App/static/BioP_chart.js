// Chart dimensions
var margin = {top: 50, right: 50, bottom: 50, left: 50}
var width = 880
var height = 550

// Rectangle dimensions
var rect_width = (width - (margin.left + margin.right))/(x_data.length + 5);

//Scale Creation
var y_scale = d3.scaleLinear()
    .domain([0, (Math.max(...y_data) + 5)])
    .range([(height - (margin.top + margin.bottom)), 0]);

var x_scale = d3.scaleBand()
    .domain(x_data)
    .range([0, (width - (margin.left + margin.right))])

var c_scale = d3.scaleSequential(d3.interpolateSpectral)
    .domain([0, 1])

var y_axis = d3.axisLeft(y_scale);
var x_axis = d3.axisBottom(x_scale);

// Chart Background
var svg = d3.select("#chart_container")
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .style("background-color", "#ffe6b3")

svg.append("rect")
    .attr("width", width - (margin.left + margin.right))
    .attr("height", height - (margin.top + margin.bottom))
    .attr("transform", 'translate(' + margin.left + "," + margin.top + ')')
    .attr("fill", "white")

var chart = svg.append('g')
    .attr("width", width - (margin.left + margin.right))
    .attr("height", height - (margin.top + margin.bottom))
    .attr("class", "chart")
    .attr("transform", 'translate(' + margin.left + "," + margin.top + ')')

// Adding Data
chart.append("g")
    .selectAll(".chart")
    .data(x_data)
    .enter()
    .append("rect")
    .attr("transform", function() {
        val = (((width - (margin.left + margin.right))/x_data.length)/2) - (rect_width/2)
        return "translate(" + val + ",0)"
    })
    .attr("x", function(d) {
        return x_scale(d);
    })
    .attr("y", function(d, i) {
        return y_scale(y_data[i])
    })
    .attr("height", function(d, i) {
        return y_scale(0) - y_scale(Number(y_data[i]))
    })
    .attr("width", function() {
        return rect_width
    })
    .style("fill", function(d, i) {
        return c_scale((1/x_data.length)*i)
    });

// Adding Axes
svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + (margin.top + (height - (margin.top + margin.bottom))) + ")")
    .call(x_axis);

svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
    .call(y_axis);

// Adding Title
svg.append("text")
    .attr("y", 0)
    .attr("x", width/2)
    .attr("dy", "1em")
    .style("text-anchor", "middle")
    .style("font-size", "30px")
    .text(title + ": " + file)





