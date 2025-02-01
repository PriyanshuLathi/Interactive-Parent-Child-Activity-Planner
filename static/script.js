document.addEventListener("DOMContentLoaded", function () {
  const predictionForm = document.getElementById("predictionForm");
  const predictedOutcome = document.getElementById("predictedOutcome");

  predictionForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(predictionForm);

    fetch("/predict", {
      method: "POST",
      body: new URLSearchParams(formData),
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data['Predicted Hobby']) {
          predictedOutcome.textContent = "Predicted Hobby: " + data['Predicted Hobby'];
        } else if (data.error) {
          predictedOutcome.textContent = "Error: " + data.error;
        }
      })
      .catch((error) => {
        predictedOutcome.textContent = "Error: Unable to predict.";
        console.error("Fetch error:", error);
      });
  });
});
