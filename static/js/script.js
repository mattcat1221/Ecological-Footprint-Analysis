
let data;
let renderGraph;

var map = L.map('map').setView([30, 20], 1);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

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

        let mapkey = '25b794c90fa551d142661753b59631e6';

        //let countryUrl = `http://api.openweathermap.org/geo/1.0/direct?q=London&limit=1&appid=${mapkey}`
        //let countryUrl = `http://api.openweathermap.org/geo/1.0/direct?q=United%20States%20of%20America&limit=1&appid=${mapkey}`

        fetch(countryUrl).then(data => data.json()).then(data => {
            console.log(data);
        })

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

