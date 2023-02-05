function addFields(val) {
    let value = val.value;
    console.log(value);
    let container = document.getElementById("dynamic_input_field_container"); // Get the element where the inputs will be added to

    // Remove every child it had before
    while (container.hasChildNodes()) {
        container.removeChild(container.lastChild);
    }

    if (value === "Website") {
        let elChild = document.createElement("div");
        elChild.innerHTML = `
                            <div>
                                <div class="form-floating mb-4">
                                    <input type="text" class="form-control" id="website_name" name="website_name"
                                           placeholder="website name">
                                    <label for="website_name">Website name</label>
                                </div>
                                <div class="form-floating mb-4">
                                    <input type="text" class="form-control" id="website_url" name="website_url"
                                           placeholder="url">
                                    <label for="website_url">Website URL</label>
                                </div>
                            </div>`;
        container.appendChild(elChild);
    } else if (value === "Desktop application") {
        let elChild = document.createElement("div");
        elChild.innerHTML = `
                            <div>
                                <div class="form-floating mb-4">
                                    <input type="text" class="form-control" id="application_name" name="application_name"
                                           placeholder="application name">
                                    <label for="application_name">Application name</label>
                                </div>
                            </div>`;
        container.appendChild(elChild);
    } else if (value === "Game") {
        let elChild = document.createElement("div");
        elChild.innerHTML = `
                            <div>
                                <div class="form-floating mb-4">
                                    <input type="text" class="form-control" id="game_name" name="game_name"
                                           placeholder="game name">
                                    <label for="game_name">Game name</label>
                                </div>
                                <div class="form-floating mb-4">
                                    <input type="text" class="form-control" id="game_developer" name="game_developer"
                                           placeholder="game developer">
                                    <label for="game_developer">Game developer</label>
                                </div>
                            </div>`;
        container.appendChild(elChild);
    }
};

function generatePasswordHandler() {
    $.ajax({
        type: 'GET',
        url: '/generate-password/',
        success: function (data) {
            document.getElementsByName('password')[0].value = data.password;
        }
    });
};

function toggleView(id) {
    const input = document.getElementById(id);
    const icon = document.getElementById(`icon-${id}`)
    if (input.type === "password") {
        input.type = "text";
        icon.classList.remove("fa-eye")
        icon.classList.add("fa-eye-slash")
    } else {
        input.type = "password";
        icon.classList.remove("fa-eye-slash")
        icon.classList.add("fa-eye")
    }
}