document.getElementById("contact-form").addEventListener("submit", function (e) {
    e.preventDefault();
    document.getElementById("form-message").textContent = "Thanks for reaching out! I’ll get back to you soon.";
    this.reset();
  });
  