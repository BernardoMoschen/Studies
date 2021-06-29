<template>
    <div class="container">
        <h1>Login</h1>
        <form>
            <div class="form-group">
                <label for="email">E-mail</label>
                <input type="email" class="form-control" v-model="usuario.email">
            </div>
            <div class="form-group">
                <label for="senha">Senha</label>
                <input type="password" class="form-control" v-model="usuario.senha">
            </div>
            <button type='submit' class="btn btn-primary brn-block"> 
                Logar 
            </button>
            <div>
            <router-link :to="{name: 'novo.usuario'}">
                Não possui cadastro? Cadastre-se aqui!
            </router-link>
            </div>
        </form>
    </div>
</template> 
<script>
export default {
    data() {
        return {
            usuario: {}
        }
    }
}
</script>