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
  // Get the canvas element
  const ctx1 = document.getElementById("totaal").getContext("2d");
  const ctx2 = document.getElementById("geboorte").getContext("2d");
  const ctx3 = document.getElementById("sterfte").getContext("2d");
  const ctx4 = document.getElementById("voedsel").getContext("2d");
  const ctx5 = document.getElementById("vervuiling").getContext("2d");
  const ctx6 = document.getElementById("land").getContext("2d");
  const ctx7 = document.getElementById("diefstal").getContext("2d");
  const ctx8 = document.getElementById("verdwaling").getContext("2d");

  try {
    // Fetch data from data.json and use destructuring for clarity
    const { years, populationData } = await fetchData();

    // Create the chart
    const totaal = new Chart(ctx1, {
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

    const geboorte = new Chart(ctx2, {
      type: "line",
      data: {
        labels: years,
        datasets: [
          {
            label: "Geboorte",
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

    const sterfte = new Chart(ctx3, {
      type: "line",
      data: {
        labels: years,
        datasets: [
          {
            label: "Sterfte",
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

    const voedsel = new Chart(ctx4, {
      type: "line",
      data: {
        labels: years,
        datasets: [
          {
            label: "Voedselaanbod",
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

    const vervuiling = new Chart(ctx5, {
      type: "line",
      data: {
        labels: years,
        datasets: [
          {
            label: "Vervuild zeewater",
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

    const land = new Chart(ctx6, {
      type: "line",
      data: {
        labels: years,
        datasets: [
          {
            label: "Landoppervlakte",
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

    const diefstal = new Chart(ctx7, {
      type: "line",
      data: {
        labels: years,
        datasets: [
          {
            label: "Gestolen pinguïns",
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

    const verdwaling = new Chart(ctx8, {
      type: "line",
      data: {
        labels: years,
        datasets: [
          {
            label: "Verdwaalde pinguïns",
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

    const graphs = [
      totaal,
      geboorte,
      sterfte,
      voedsel,
      vervuiling,
      land,
      diefstal,
      verdwaling,
    ];

    const startAnimationButton = document.getElementById("startAnimation");
    let yearIndex = 0;
    let animationInterval;

    startAnimationButton.addEventListener("click", () => {
      startAnimationButton.disabled = true;
      animationInterval = setInterval(animateGraph, 200); // Adjust animation speed (milliseconds)
    });

    function animateGraph() {
      if (yearIndex < years.length) {
        for (let i = 0; i < graphs.length; i++) {
          graphs[i].data.datasets[0].data[yearIndex] =
            populationData[yearIndex];
          graphs[i].update();
        }
      } else {
        clearInterval(animationInterval);
        startAnimationButton.disabled = false;
      }
    }
  } catch (error) {
    console.error("Error loading data:", error);
    // Handle the error gracefully, e.g., display an error message to the user
  }
});
