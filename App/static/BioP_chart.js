// Chart dimensions
var margin = {top: 50, right: 50, bottom: 50, left: 50}
var width = 880
var height = 550

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
    .attr("transform", 'translate(' + margin.left + "," + margin.top + ')')


// Adding Title
svg.append("text")
    .attr("y", 0)
    .attr("x", width/2)
    .attr("dy", "1em")
    .style("text-anchor", "middle")
    .style("font-size", "30px")
    .text(title)


