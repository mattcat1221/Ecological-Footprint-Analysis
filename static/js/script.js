
let data;
let renderGraph;

const init = async () => {
    data = await (await fetch('/api/v1.0/ecological_data')).json();

    main.innerHTML = `
        <select id="features" onchange="renderGraph()"></select>
        <div id="chart"></div>`;

    Object.keys(data[0]).filter(col => col != 'Country').forEach(feature => {
        features.innerHTML += `<option>${feature}</option>`
    });

    renderGraph = () => {
        
        let option = document.querySelector('select').value
        let maxVal = Math.max(...data.map(obj => [obj[option]]));
        let minVal = Math.min(...data.map(obj => [obj[option]]));

        selCountries = [
            data.find(obj => obj[option] == minVal).Country,
            "United States of America",
            data.find(obj => obj[option] == maxVal).Country
        ];

        selValues = [
            minVal,
            data.find(obj => obj.Country == "United States of America")[option],
            maxVal
        ];

        var plotData = [
            {
                x: selCountries,
                y: selValues,
                type: 'bar',
                marker: {
                    color: ['green','yellow','orange']
                }
            }
        ];

        Plotly.newPlot('chart', plotData, {});
    };

    renderGraph();

}

init();