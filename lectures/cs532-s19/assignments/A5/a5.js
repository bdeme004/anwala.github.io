/* eslint-env browser */
/* eslint-env es6*/
/* global d3 */
/* code modified from:
https://bl.ocks.org/mbostock/b1f0ee970299756bc12d60aedf53c13b
https://bl.ocks.org/mbostock/f584aa36df54c451c94a9d0798caed35
*/

var canvas = document.getElementById("canvas"),
    context = canvas.getContext("2d"),
    width = canvas.width,
    height = canvas.height;

var simulation = d3.forceSimulation()
    .force("link", d3.forceLink().id(function (d) {
        return d.id;
    }))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter());


d3.json("karate_club.json", function (error, graph) {
    if (error) throw error;

    simulation
        .nodes(graph.nodes)
        .on("tick", ticked);

    simulation.force("link")
        .links(graph.links);

});

function ticked() {
    context.clearRect(0, 0, width, height);
    context.save();
    context.translate(width / 2, height / 2 + 40);

    simulation.force("link").links().forEach(drawLink);
    simulation.nodes().forEach(drawNode);

    context.restore();
}

function drawLink(d) {
    context.beginPath();
    context.moveTo(d.source.x, d.source.y);
    context.lineTo(d.target.x, d.target.y);
    context.strokeStyle = "#aaa";
    context.stroke();
}

function drawNode(d) {
    context.beginPath();
    context.moveTo(d.x + 3, d.y);
    context.arc(d.x, d.y, 3, 0, 2 * Math.PI);
    context.fillStyle = (d.club == "Mr. Hi") ? "red" : "green";
    context.fill();
}


/* exported splitClub */
function splitClub() {
    simulation
        .nodes(simulation.nodes())
        .on("tick", ticked);

    var g_links = simulation.force("link").links()
        .filter(function(link) {
            return link.source.club == link.target.club
        });
    simulation.force("link").links(g_links);
}


