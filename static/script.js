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
  let divs = []; // a list of div elements from HTML
  let years_list = []; // a list of lists of years per variable
  let data_list = []; // a list of lists of data per variable
  let data_list2 = []; // a list of lists of secondary data per variable

  try {
    const response = await fetch("./static/data.json");
    const data = await response.json();

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
    } // create the divs in HTML

    Ids.forEach((id) => {
      createGraphDiv(id);
      divs.push(document.getElementById(id).getContext("2d"));
    }); // store div elements from HTML

    for (let variable in data) {
      years_list.push(data[variable].years); // save the years per variable
      data_list.push(data[variable].data); // save the data per variable

      if (data[variable].data2) {
        data_list2.push(data[variable].data2); // save the secondary data per variable
      } else {
        data_list2.push(null); // if there's no secondary data, store null
      }
    }

    const charts = [];

    for (let i = 0; i < divs.length; i++) {
      const datasets = [
        {
          label: Ids[i],
          data: Array(years_list[i].length).fill(0), // Initialize data with zeros
          backgroundColor: `rgba(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.random()})`,
          borderColor: `rgba(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, 1)`,
          borderWidth: 1,
        }
      ];

      // If there's secondary data, add it as a separate dataset
      if (data_list2[i]) {
        datasets.push({
          label: `Pinguïns`,
          data: Array(years_list[i].length).fill(0), // Initialize data with zeros
          backgroundColor: `rgba(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, 0.2)`,
          borderColor: `rgba(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, 1)`,
          borderWidth: 1,
        });
      }

      charts[i] = new Chart(divs[i], {
        type: "line",
        data: {
          labels: years_list[i],
          datasets: datasets,
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

    const startAnimationButton = document.getElementById("startAnimation"); // Define the button
    startAnimationButton.addEventListener("click", function () {
      try {
        for (let i = 0; i < data_list.length; i++) {
          let j = 0;
          const interval = setInterval(function () {
            if (j < data_list[i].length) {
              charts[i].data.datasets[0].data[j] = data_list[i][j];
              if (data_list2[i]) {
                charts[i].data.datasets[1].data[j] = data_list2[i][j];
              }
              charts[i].update();
              j++;
            } else {
              clearInterval(interval);
            }
          }, 10*(200/years_list[8].length)); // 
        }
      } catch (error) {
        console.error("Error loading data:", error); // Catch all errors, there are no, I'm perfect
      }
    });
  } catch (error) {
    console.error("Error loading data:", error); // catch all errors, there a no, im perfect
  }
});
