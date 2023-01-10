function submit() {
    fetch("login.php")
    .then((response) => {
        if (response.ok) {
            throw new Error("Oppsie Diasy");
        }
        return response.json();
    })
    .then((data) => {
        console.log(data);
    })
    .catch((error) => {
        console.log(error);
    });
}