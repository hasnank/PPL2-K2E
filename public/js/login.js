var hid = true;
$(".error-span").hide();

function hai() {
    var id = document.getElementById("id").value;
    if (id == "mahasiswa") {
        window.location = "mhs-jadwalsidang.html";
        return false;
    } else
    if (id == "dosen") {
        window.location = "dsn-isi-constraints.html";
        return false;
    } else
    if (id == "tuif") {
        window.location = "tu-add.html";
        return false;
    } else {
        if (hid) {
            $(".error-span").fadeIn();
        }
        return false;
    }
}