function cpf_mask() {
    var cpf = document.getElementById("id_cpf");

    if (cpf.value.length == 3 || cpf.value.length == 7) {
        cpf.value += ".";
    }
    if (cpf.value.length == 11) {
        cpf.value += "-";
    }
}


function phone_mask() {
    var phone = document.getElementById("id_phone");
    if (phone.value.length == 3) {
        phone.value += ") ";
    }
    if (phone.value.length == 10) {
        phone.value += "-";
    }
}

function phone_mask_focus() {
    var phone = document.getElementById("id_phone");
    if (phone.value.length == 0){
        phone.value += "(";
    }
}

function phone_mask_blur(){
    var phone = document.getElementById("id_phone");
    if (phone.value.length == 1){
        phone.value = null;
    }
}