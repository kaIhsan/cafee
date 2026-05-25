function cekForm() {
    let nama = document.getElementById("nama").value;
    if (nama.length < 3) {
        alert("Nama tidak boleh terlalu pendek!");
        return false;
    }
    return true;
}