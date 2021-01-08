const formValidation = (() => {
    const username = document.querySelector("input[name='username']");
    const first_name = document.querySelector("input[name='first_name']");
    const last_name = document.querySelector("input[name='last_name']");
    const email = document.querySelector("input[name='email']");
    const password = document.querySelector("input[name='password1']");
    const confirmPassword = document.querySelector("input[name='password2']");
    let isValid = true;

    function checkUsername() {
        const p = document.createElement('p');
        p.classList.add('error');
        if (username.value === '') {
            isValid = false;
            username.style.border = '2px solid red';
            p.textContent = 'Field is required.';
            username.parentNode.appendChild(p);
            return;
        }
    }
    function checkFirstName() {
        const p = document.createElement('p');
        p.classList.add('error');
        if (first_name.value === '') {
            isValid = false;
            first_name.style.border = '2px solid red';
            p.textContent = 'Field is required.';
            first_name.parentNode.appendChild(p);
            return;
        }
    }
    function checkLastName() {
        const p = document.createElement('p');
        p.classList.add('error');
        if (last_name.value === '') {
            isValid = false;
            last_name.style.border = '2px solid red';
            p.textContent = 'Field is required.';
            last_name.parentNode.appendChild(p);
            return;
        }
    }
    function checkUsername() {
        const p = document.createElement('p');
        p.classList.add('error');
        if (username.value === '') {
            isValid = false;
            username.style.border = '2px solid red';
            p.textContent = 'Field is required.';
            username.parentNode.appendChild(p);
            return;
        }
    }

    function checkEmail() {
        const p = document.createElement('p');
        p.classList.add('error');
        const reg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if (email.value === '') {
            isValid = false;
            email.style.border = '2px solid red';
            p.textContent = 'Field is required.';
            email.parentNode.appendChild(p);
            return;
        }
        if (reg.test(String(email.value).toLowerCase())) {
            return;
        } else {
            isValid = false;
            p.textContent = 'Please enter a valid email address.';
            email.parentNode.appendChild(p);
            return;
        }
    }

    function checkPassword() {
        const p = document.createElement('p');
        p.classList.add('error');
        const reg = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
        if (password.value === '') {
            isValid = false;
            password.style.border = '2px solid red';
            p.textContent = 'Field is required.';
            password.parentNode.appendChild(p);
            return;
        }
        if (reg.test(String(password.value))) {
            return;
        } else {
            isValid = false;
            password.style.border = '2px solid red';
            p.textContent =
                'Your password must contain at least 8 characters and contain one uppercase letter, one lowercase letter, and a digit.';
            password.parentNode.appendChild(p);
            return;
        }
    }
    function checkConfirmedPassword() {
        const p = document.createElement('p');
        p.classList.add('error');
        const reg = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/;
        if (confirmPassword.value === '') {
            isValid = false;
            confirmPassword.style.border = '2px solid red';
            p.textContent = 'Field is required.';
            confirmPassword.parentNode.appendChild(p);
            return;
        }
        if (confirmPassword.value === password.value) {
            return;
        } else {
            isValid = false;
            confirmPassword.style.border = '2px solid red';
            p.textContent = 'Please make sure your passwords match.';
            confirmPassword.parentNode.appendChild(p);
            return;
        }
    }
    function resetStyle() {
        const inputs = document.querySelectorAll('input');
        inputs.forEach((input) => {
            input.style = '';
            try {
                input.parentNode.removeChild(input.parentNode.querySelector('.error'));
                input.parentNode.removeChild(input.parentNode.querySelector('.error'));
            } catch {}
        });
    }

    function checkForm(e) {
        const form = document.querySelector('form');
        e.preventDefault();
        isValid = true;
        resetStyle();
        checkUsername();
        checkFirstName();
        checkLastName();
        checkEmail();
        checkPassword();
        checkConfirmedPassword();
        if (isValid) {
            form.submit();
        }
    }

    document.querySelector('button[name="register"]').addEventListener('click', checkForm);
})();
