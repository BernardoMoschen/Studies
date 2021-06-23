import Vue from 'vue';

Vue.directive('meu-transform', {

  bind(elDom, binding, vnode) {
    let current = 0;
    elDom.addEventListener('dblclick', function() {
      let incremento = binding.value || 90

      current += incremento
      this.style.transform = `rotate(${current}deg)`;
      if (binding.modifiers.animate) elDom.style.transition = "transform 0.5s"
    });
  }
})
