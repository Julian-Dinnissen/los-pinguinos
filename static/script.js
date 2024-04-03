// async function fetchDataAndSaveLists() {
//   fetch("./static/data.json")
//     .then((response) => response.json())
//     .then((data) => {
//       // Iterate over each variable
//       for (let variable in data) {
//         // Extract years and data for the current variable
//         const years = data[variable].years;
//         const variableData = data[variable].data;

//         // Create lists to store years and data for the current variable
//         const yearsList = [];
//         const dataList = [];

//         // Push years and data into respective lists
//         for (let i = 0; i < years.length; i++) {
//           yearsList.push(years[i]);
//           dataList.push(variableData[i]);
//         }

//         // Output the lists
//         console.log(`${variable}_years: `, yearsList);
//         console.log(`${variable}_data: `, dataList);
//       }

//       const varList = [];
//       for (let variable in data) {
//         varList.push(variable);
//       }
//       console.log(varList);
//     })
//     .catch((error) => console.error("Error fetching JSON:", error));
// }
// await fetchDataAndSaveLists();

async function fetchData() {
  try {
    const response = await fetch("./static/data.json");
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error; // Re-throw the error for further handling
  }
}

document.addEventListener("DOMContentLoaded", async function () {
  let Ids = []; // a list of graph names
  let divs = []; // a list of div elements from html
  let years_list = []; // a list of lists of years per variable
  let data_list = []; // a list of lists of data per variable

  const data = await fetchData(); // save the data from the json as a variable

  for (let variable in data) {
    Ids.push(variable);
  }

  function createGraphDiv(canvasId) {
    var graphContainer = document.querySelector(".graph-container");
    var graphDiv = document.createElement("div");
    graphDiv.className = "graph";

    var canvas = document.createElement("canvas");
    canvas.id = canvasId;
    canvas.width = "400";
    canvas.height = "200";

    graphDiv.appendChild(canvas);
    graphContainer.appendChild(graphDiv);
  } // create the divs in html

  Ids.forEach((id) => {
    createGraphDiv(id);
    divs.push(document.getElementById(id).getContext("2d"));
  }); //store div elements from html

  try {
    for (let variable in data) {
      years_list.push(data[variable].years); // save the years per variable
      data_list.push(data[variable].data); // save the data per variable
    }

    const charts = [];

    for (let i = 0; i < divs.length; i++) { 
      charts[i] = new Chart(divs[i], {
        type: "line",
        data: {
          labels: years_list[i],
          datasets: [
            {
              label: Ids[i],
              data: Array(years_list[i].length).fill(0), // Initialize data with zeros
              backgroundColor: "rgba(255, 99, 132, 0.2)",
              borderColor: "rgba(255, 99, 132, 1)",
              borderWidth: 1,
            },
          ],
        },
        options: {
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      });
    } // create a chart per variable in Ids

  

    const startAnimationButton = document.getElementById("startAnimation"); //define the button
    startAnimationButton.addEventListener("click", function () {
      for (let i = 0; i < data_list.length; i++) {
        let j = 0;
        const interval = setInterval(function () {
          if (j < data_list[i].length) {
            charts[i].data.datasets[0].data[j] = data_list[i][j];
            charts[i].update();
            j++;
          } else {
            clearInterval(interval);
          }
        }, 10*(200/years_list[8].length));
      }
    }); // update the charts when button is clicked
  } catch (error) {
    console.error("Error loading data:", error); // catch all errors, there a no, im perfect
  }
});
