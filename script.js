// -----------------------------
// 1. SIDEBAR ACTIVE MENU
// -----------------------------
var menuItems = document.querySelectorAll(".menu-item");

for (var i = 0; i < menuItems.length; i++) {
    menuItems[i].onclick = function () {
        for (var j = 0; j < menuItems.length; j++) {
            menuItems[j].classList.remove("active");
        }
        this.classList.add("active");
    };
}


// -----------------------------
// 2. DARK MODE TOGGLE
// -----------------------------
var darkBtn = document.querySelectorAll(".icon-btn")[0];

darkBtn.onclick = function () {
    document.body.classList.toggle("dark-mode");
};


// -----------------------------
// 3. SEARCH FUNCTION (REAL FILTER)
// -----------------------------
var searchInput = document.querySelector(".search input");

searchInput.onkeyup = function () {
    var value = searchInput.value.toLowerCase();

    for (var i = 0; i < menuItems.length; i++) {
        var text = menuItems[i].innerText.toLowerCase();

        if (text.indexOf(value) > -1) {
            menuItems[i].style.display = "flex";
        } else {
            menuItems[i].style.display = "none";
        }
    }
};


// -----------------------------
// 4. LOGOUT BUTTON
// -----------------------------
var logoutBtn = document.querySelectorAll(".icon-btn")[2];

logoutBtn.onclick = function () {
    var confirmLogout = confirm("Do you really want to logout?");
    
    if (confirmLogout) {
        alert("Logout successful!");
    }
};


// -----------------------------
// 5. DYNAMIC GREETING
// -----------------------------
var greeting = document.querySelector(".welcome h1");
var hour = new Date().getHours();

if (hour < 12) {
    greeting.innerText = "Good Morning, Student ☀️";
} 
else if (hour < 18) {
    greeting.innerText = "Good Afternoon, Student 🌤️";
} 
else {
    greeting.innerText = "Good Evening, Student 🌙";
}


// -----------------------------
// 6. BUTTON CLICK ACTIONS
// -----------------------------
var primaryBtn = document.querySelector(".primary");
var secondaryBtn = document.querySelector(".secondary");

primaryBtn.onclick = function () {
    alert("Redirecting to assignment submission...");
};

secondaryBtn.onclick = function () {
    alert("Resuming your quiz...");
};

