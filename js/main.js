document.addEventListener("DOMContentLoaded", function () {
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  function closeAllRdvMenus() {
    document.querySelectorAll(".rdv-menu.open").forEach(function (m) {
      m.classList.remove("open");
      var b = m.querySelector(".rdv-toggle");
      if (b) b.setAttribute("aria-expanded", "false");
    });
  }
  document.querySelectorAll(".rdv-toggle").forEach(function (btn) {
    var menu = btn.closest(".rdv-menu");
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var isOpen = menu.classList.contains("open");
      closeAllRdvMenus();
      if (!isOpen) {
        menu.classList.add("open");
        btn.setAttribute("aria-expanded", "true");
      }
    });
  });
  document.addEventListener("click", closeAllRdvMenus);
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeAllRdvMenus();
  });

  var form = document.querySelector(".contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = form.querySelector(".form-status");
      var submitBtn = form.querySelector("button[type=submit]");
      var formData = new FormData(form);
      var payload = Object.fromEntries(formData);

      if (status) status.textContent = "Envoi en cours...";
      if (submitBtn) submitBtn.disabled = true;

      fetch("https://api.web3forms.com/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(payload)
      })
        .then(function (response) { return response.json(); })
        .then(function (data) {
          if (data.success) {
            if (status) status.textContent = "Merci, votre message a bien été envoyé. Le cabinet vous recontactera rapidement.";
            form.reset();
          } else {
            if (status) status.textContent = "Une erreur est survenue lors de l'envoi. Merci de réessayer ou de nous appeler directement.";
          }
        })
        .catch(function () {
          if (status) status.textContent = "Une erreur est survenue lors de l'envoi. Merci de réessayer ou de nous appeler directement.";
        })
        .finally(function () {
          if (submitBtn) submitBtn.disabled = false;
        });
    });
  }

  var yearEl = document.querySelector("[data-year]");
  if (yearEl) { yearEl.textContent = new Date().getFullYear(); }
});
