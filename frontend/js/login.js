document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");

    form.addEventListener("submit", (e) => {
        e.preventDefault();

        const username = document.getElementById("username").value.trim();
        const password = document.getElementById("password").value.trim();

        // Akun admin contoh
        const adminUsername = "admin";
        const adminPassword = "12345";

        if (
            username === adminUsername &&
            password === adminPassword
        ) {
            alert("Login Admin Berhasil!");

            // Pindah ke dashboard
            window.location.href = "dashboard.html";
        } else {
            alert("Username atau password salah!");
        }
    });
});