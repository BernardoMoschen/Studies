import Vue from 'vue';

Vue.directive('meu-transform', {

  bind(elDom, binding, vnode) {
    let current = 0;
    elDom.addEventListener('dblclick', function() {
      current+=90;
      this.style.transform = `rotate(${current}deg)`;
    });
  }
})
