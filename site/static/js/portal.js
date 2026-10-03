/**
 * Minimalist controller for theme switching, list/grid toggle, and search filter.
 */

(function () {
  "use strict";

  // Theme Management
  function initTheme() {
    const themeBtn = document.getElementById("theme-toggle");
    if (!themeBtn) return;

    function updateLabel() {
      const isDark = document.documentElement.classList.contains("dark");
      themeBtn.textContent = isDark ? "Light" : "Dark";
    }

    themeBtn.addEventListener("click", () => {
      const isDark = document.documentElement.classList.toggle("dark");
      localStorage.setItem("theme-mode", isDark ? "dark" : "light");
      updateLabel();
    });

    updateLabel();
  }

  // View Mode Toggle (List vs Grid)
  function initViewToggle() {
    const btnList = document.getElementById("toggle-list");
    const btnGrid = document.getElementById("toggle-grid");
    const viewList = document.getElementById("view-list");
    const viewGrid = document.getElementById("view-grid");

    if (!btnList || !btnGrid || !viewList || !viewGrid) return;

    function setView(mode) {
      if (mode === "grid") {
        viewList.style.display = "none";
        viewGrid.style.display = "grid";
        btnGrid.classList.add("active");
        btnList.classList.remove("active");
        localStorage.setItem("view-mode", "grid");
      } else {
        viewList.style.display = "block";
        viewGrid.style.display = "none";
        btnList.classList.add("active");
        btnGrid.classList.remove("active");
        localStorage.setItem("view-mode", "list");
      }
    }

    btnList.addEventListener("click", () => setView("list"));
    btnGrid.addEventListener("click", () => setView("grid"));

    const savedView = localStorage.getItem("view-mode") || "list";
    setView(savedView);
  }

  // Search Filter
  function initSearchFilter() {
    const searchInput = document.getElementById("course-search");
    const items = document.querySelectorAll(".course-item");
    if (!searchInput || !items.length) return;

    searchInput.addEventListener("input", (e) => {
      const q = e.target.value.toLowerCase().trim();
      items.forEach((item) => {
        const text = (item.getAttribute("data-search") || item.innerText).toLowerCase();
        item.style.display = text.includes(q) ? "" : "none";
      });
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    initTheme();
    initViewToggle();
    initSearchFilter();
  });
})();
