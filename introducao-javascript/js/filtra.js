var campoFiltro = document.querySelector("#filtrar-tabela");

campoFiltro.addEventListener("input", function() {
    let pacientes = document.querySelectorAll(".paciente");

    if (this.value.length > 0) {
        for (let paciente of pacientes) {   
            paciente.classList.remove("invisivel");    
        }
    }
    for (let paciente of pacientes) {
        paciente.classList.add("invisivel");
    }
});