function checkStrength() {

    let password = document.getElementById("password").value;
    let strength = "Weak";

    if (password.length >= 8) {
        strength = "Medium";
    }

    if (password.match(/[A-Z]/) && 
        password.match(/[0-9]/) && 
        password.match(/[@$!%*?&]/)) {
        strength = "Strong";
    }

    document.getElementById("result").innerText = strength;
}