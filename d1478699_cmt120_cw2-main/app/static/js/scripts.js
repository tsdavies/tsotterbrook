document.addEventListener("DOMContentLoaded", function () {
  try {
    ("use strict");

    // Select all forms that require validation
    const forms = document.querySelectorAll(".needs-validation");

    // Add validation handling for each form
    Array.from(forms).forEach((form) => {
      // Add a 'submit' event listener to the form
      form.addEventListener(
        "submit",
        (event) => {
          if (!form.checkValidity()) {
            // Prevent form submission if it is invalid
            event.preventDefault();
            event.stopPropagation();
          }
          // Add 'was-validated' class to show validation feedback
          form.classList.add("was-validated");
        },
        false,
      );

      // Add 'blur' event listeners to all form inputs
      const inputs = form.querySelectorAll("input, textarea, select");
      Array.from(inputs).forEach((input) => {
        input.addEventListener("blur", () => {
          // Add 'is-invalid' class for invalid inputs, or remove it for valid inputs
          if (!input.checkValidity()) {
            input.classList.add("is-invalid");
          } else {
            input.classList.remove("is-invalid");
          }
        });
      });
    });

    // Initialise Bootstrap tooltips if Bootstrap is loaded
    if (typeof bootstrap !== "undefined" && bootstrap.Tooltip) {
      const tooltipTriggerList = [].slice.call(
        document.querySelectorAll('[data-bs-toggle="tooltip"]'),
      );
      tooltipTriggerList.map((tooltipTriggerEl) => {
        return new bootstrap.Tooltip(tooltipTriggerEl);
      });
    } else {
      // Log a warning if Bootstrap Tooltip is unavailable
      console.warn("Bootstrap Tooltip not found");
    }
  } catch (error) {
    // Log errors to the console
    console.error("Error in form validation script:", error);
  }
});
