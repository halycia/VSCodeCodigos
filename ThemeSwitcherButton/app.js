'use strict'
/*antes de adicionar o manipulador de eventos, você precisa de uma referencia para o botao*/
/*const switcher = document.querySelector('.btn');/*pega a referencia do botao*/

/*switcher.addEventListener('click', function() {
    document.body.classList.toggle('dark-theme')

    var className = document.body.className;
    if(className == "light-theme") {
        this.textContent = "Dark";
    }
    else {
        this.textContent = "Light";
    }
    console.log('current class name: ' + className);
});*/

 // Get the checkbox element
 const checkbox = document.querySelector("input[type='checkbox']");

 // Add a change event listener to the checkbox
 checkbox.addEventListener("change", function() {
   // Toggle the 'dark-theme' class on the body element
   document.body.classList.toggle("dark-theme");
 });
