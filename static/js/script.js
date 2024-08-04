
let data; any
let renderGraph

async function init() {

    data = await (await fetch('/api/v1.0/ecological_data')).json();

    main.innerHTML = `
        <select id="features" onchange="renderGraph()"></select>
        <div id="chart"></div>`;

    Object.keys(data[0]).filter(col => col != 'Country').forEach(feature => {
        features.innerHTML += `<option>${feature}</option>`;
    });

    renderGraph = async () => {

        let option = document.querySelector('select').value;
        let maxVal = Math.max(...data.map(obj => [obj[option]]));
        let minVal = Math.min(...data.map(obj => [obj[option]]));

        selCountries = [
            data.find(obj => obj[option] == minVal).Country,
            "United States of America",
            data.find(obj => obj[option] == maxVal).Country
        ];

        coord = await (await fetch(`pk.eyJ1IjoibWF0dGNhdCIsImEiOiJjbHljNTd2ZHExbGhuMmpvcmgwbDRraXg5In0.9g1ekKOFpqTIw1Z0O3z8Dg`)).json();


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
                    color: ['green', 'yellow', 'orange']
                }
            }
        ];

        Plotly.newPlot('chart', plotData, {});
    };

    renderGraph();

}

init();
let data; any 
let renderGraph;

const init = async () => {
    try {
        // Fetch ecological data from API
        console.log('Fetching data from API...');
        const response = await fetch('/api/v1.0/ecological_data');
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        data = await response.json();
        console.log('Data fetched:', data);

        // Set up the main container
        const main = document.getElementById('main');
        main.innerHTML = `
            <select id="features" onchange="renderGraph()"></select>
            <div id="chart"></div>`;

        // Populate the dropdown with feature options
        const features = document.getElementById('features');
        Object.keys(data[0]).filter(col => col != 'Country').forEach(feature => {
            features.innerHTML += `<option>${feature}</option>`;
        });

        // Define the renderGraph function
        renderGraph = async () => {
            const option = document.querySelector('select').value;

            // Find min and max values and their corresponding countries
            const maxVal = Math.max(...data.map(obj => obj[option]));
            const minVal = Math.min(...data.map(obj => obj[option]));

            const selCountries = [
                data.find(obj => obj[option] === minVal).Country,
                "United States of America",
                data.find(obj => obj[option] === maxVal).Country
            ];

            // Ensure coord API call works correctly (using placeholder URL here)
            // const coord = await (await fetch(`API_URL`)).json();

            const selValues = [
                minVal,
                data.find(obj => obj.Country === "United States of America")[option],
                maxVal
            ];

            // Prepare the data for the plot
            const plotData = [
                {
                    x: selCountries,
                    y: selValues,
                    type: 'bar',
                    marker: {
                        color: ['green', 'yellow', 'orange']
                    }
                }
            ];

            // Render the plot using Plotly
            Plotly.newPlot('chart', plotData, {});
        };

        // Initial render of the graph
        renderGraph();
    } catch (error) {
        console.error('Error fetching ecological data:', error);
    }
};

// Initialize the script
init();
an