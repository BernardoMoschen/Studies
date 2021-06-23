var campoFiltro = document.querySelector("#filtrar-tabela");

campoFiltro.addEventListener("input", function() {
    var pacientes = document.querySelectorAll(".paciente");

    if (this.value.length > 0) {
        for (let paciente of pacientes) {
            var nomePacienteTd = paciente.querySelector(".info-nome").textContent
            var expressao = new RegExp(this.value, "i");

            if (expressao.test(nomePacienteTd)) {
                paciente.classList.remove("invisivel");
            } else {
                paciente.classList.add("invisivel");
            }
        }
    } else {
        for (let paciente of pacientes) {
            paciente.classList.remove("invisivel");
        }
    }
});