import Vue from 'vue';

Vue.directive('meu-transform', {

  bind(elDom, binding, node) {
    console.log('Diretiva iniciada')
    console.log(elDom)
  }
});
