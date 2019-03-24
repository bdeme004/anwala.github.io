/* eslint-env browser */
/* eslint-env es6*/
/* global d3 */

var canvas = document.querySelector("canvas"),
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

    function ticked() {
        context.clearRect(0, 0, width, height);
        context.save();
        context.translate(width / 2, height / 2 + 40);

        context.beginPath();
        graph.links.forEach(drawLink);
        context.strokeStyle = "#aaa";
        context.stroke();

        graph.nodes.forEach(drawNode);

        context.restore();
    }

});

function drawLink(d) {
    context.moveTo(d.source.x, d.source.y);
    context.lineTo(d.target.x, d.target.y);
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
    d3.json("karate_club.json", function (error, graph) {
        if (error) throw error;

        context.clearRect(0, 0, width, height);
        context.fill();

        simulation
            .nodes(graph.nodes)
            .on("tick", ticked);

        simulation.force("link")
            .links(graph.links.filter(withinClub));

        function ticked() {
            context.clearRect(0, 0, width, height);
            context.save();
            context.translate(width / 2, height / 2 + 40);

            context.beginPath();
            graph.links.forEach(drawLink);
            context.strokeStyle = "#aaa";
            context.stroke();

            graph.nodes.forEach(drawNode);

            context.restore();
        }

        function withinClub(link) {
            return (
                graph.nodes[link.source].club ==
                graph.nodes[link.target].club
            )
        }

    });
}
