let loginForm = document.getElementById('login');
let registerForm = document.getElementById('register');

function changeFormToLogin() {
    registerForm.style.display = 'none';
    loginForm.style.display = 'block';
}

function changeFormToRegister() {
    registerForm.style.display = 'block';
    loginForm.style.display = 'none';
}

