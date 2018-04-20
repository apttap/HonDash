class Icon {

    constructor(id, path_off, path_on){
        this.element = document.getElementById(id);
        this.path_off = path_off;
        this.path_on = path_on;
        var img = document.createElement("img");
        img.src = "icons/" + this.path_off;
        img.style.width = "100%";
        this.element.appendChild(img);
    }

    refresh(value){
        var img = document.createElement("img");
        img.style.width = "100%";
        img.src = "icons/" + (value > 0 ? this.path_on : this.path_off);
        this.element.innerHTML = '';
        this.element.appendChild(img);
    }
}