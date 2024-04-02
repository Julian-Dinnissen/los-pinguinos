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

// await console.log(fetchData());

document.addEventListener("DOMContentLoaded", async function () {
  // Get the canvas element

  let divs = [
    document.getElementById("totaal").getContext("2d"),
    document.getElementById("geboorte").getContext("2d"),
    document.getElementById("sterfte").getContext("2d"),
    document.getElementById("voedsel").getContext("2d"),
    document.getElementById("vervuiling").getContext("2d"),
    document.getElementById("land").getContext("2d"),
    document.getElementById("diefstal").getContext("2d"),
    document.getElementById("verdwaling").getContext("2d"),
    document.getElementById("bekering").getContext("2d"),
  ];

  try {
    const data = await fetchData();

    // console.log(data);
    // console.log(data.Populatie.years);

    const years = data.Populatie.years;
    const variableData = data.Populatie.data;

    // Create the chart
    const totaal = new Chart(divs[0], {
      type: "line",
      data: {
        labels: years,
        datasets: [
          {
            label: "Populatie",
            data: Array(years.length).fill(0), // Initialize data with zeros
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

    const startAnimationButton = document.getElementById("startAnimation");
    let yearIndex = 0;
    let animationInterval;

    startAnimationButton.addEventListener("click", () => {
      startAnimationButton.disabled = true;
      animationInterval = setInterval(animateAllGraphs, 200); // Adjust animation speed (milliseconds)
    });

    function animateAllGraphs() {
      if (yearIndex < years.length) {
        graphs.forEach((graph) => {
          animateGraph(graph);
        });
        yearIndex++;
      } else {
        clearInterval(animationInterval);
        startAnimationButton.disabled = false;
      }
    }

    function animateGraph(graph) {
      graph.data.datasets[0].data[yearIndex] = variableData[yearIndex];
      graph.update();
    }

    const graphs = [totaal];
  } catch (error) {
    console.error("Error loading data:", error);
    // Handle the error gracefully, e.g., display an error message to the user
  }
});
