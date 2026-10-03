/**
 * Controller for theme switching, list/grid toggle, search, and school/semester tag filters.
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

  // Multi-Filter Engine (Search + School Tag + Semester Tag)
  function initFilterEngine() {
    const searchInput = document.getElementById("course-search");
    const countLabel = document.getElementById("course-count");
    const resetBtn = document.getElementById("reset-filters");
    const noMatches = document.getElementById("no-matches");
    const items = document.querySelectorAll(".course-item");
    const filterButtons = document.querySelectorAll("[data-filter-group]");
    const inlineButtons = document.querySelectorAll("[data-filter-click]");

    if (!items.length) return;

    // Filter state
    let activeSchool = "all";
    let activeSemester = "all";
    let searchQuery = "";

    const totalCount = items.length;

    function updateButtonsUI() {
      filterButtons.forEach((btn) => {
        const group = btn.getAttribute("data-filter-group");
        const val = btn.getAttribute("data-filter-value");
        const isActive = (group === "school" && activeSchool === val) ||
                         (group === "semester" && activeSemester === val);
        btn.classList.toggle("active", isActive);
      });

      if (resetBtn) {
        const isFiltered = (activeSchool !== "all" || activeSemester !== "all" || searchQuery !== "");
        resetBtn.style.display = isFiltered ? "inline-block" : "none";
      }
    }

    function applyFilters() {
      let visibleCount = 0;

      items.forEach((item) => {
        const itemSchool = item.getAttribute("data-school") || "";
        const itemSemester = item.getAttribute("data-semester") || "";
        const itemSearch = (item.getAttribute("data-search") || item.innerText).toLowerCase();

        const matchSchool = (activeSchool === "all" || itemSchool === activeSchool);
        const matchSemester = (activeSemester === "all" || itemSemester === activeSemester);
        const matchSearch = (!searchQuery || itemSearch.includes(searchQuery));

        if (matchSchool && matchSemester && matchSearch) {
          item.style.display = "";
          visibleCount++;
        } else {
          item.style.display = "none";
        }
      });

      if (countLabel) {
        if (activeSchool !== "all" || activeSemester !== "all" || searchQuery !== "") {
          countLabel.textContent = `${visibleCount} of ${totalCount} items`;
        } else {
          countLabel.textContent = `${totalCount} items`;
        }
      }

      if (noMatches) {
        noMatches.style.display = (visibleCount === 0) ? "block" : "none";
      }

      updateButtonsUI();
    }

    // Filter panel click handler
    filterButtons.forEach((btn) => {
      btn.addEventListener("click", () => {
        const group = btn.getAttribute("data-filter-group");
        const val = btn.getAttribute("data-filter-value");

        if (group === "school") {
          activeSchool = val;
        } else if (group === "semester") {
          activeSemester = val;
        }
        applyFilters();
      });
    });

    // Inline tag badges click handler (click on [BULME] or [Semester 8] in table/card)
    inlineButtons.forEach((btn) => {
      btn.addEventListener("click", (e) => {
        e.stopPropagation();
        const type = btn.getAttribute("data-filter-click");
        const val = btn.getAttribute("data-value");

        if (type === "school") {
          activeSchool = (activeSchool === val) ? "all" : val;
        } else if (type === "semester") {
          activeSemester = (activeSemester === val) ? "all" : val;
        }
        applyFilters();
      });
    });

    // Search query input handler
    if (searchInput) {
      searchInput.addEventListener("input", (e) => {
        searchQuery = e.target.value.toLowerCase().trim();
        applyFilters();
      });
    }

    // Reset filters
    if (resetBtn) {
      resetBtn.addEventListener("click", () => {
        activeSchool = "all";
        activeSemester = "all";
        searchQuery = "";
        if (searchInput) searchInput.value = "";
        applyFilters();
      });
    }

    applyFilters();
  }

  document.addEventListener("DOMContentLoaded", () => {
    initTheme();
    initViewToggle();
    initFilterEngine();
  });
})();
