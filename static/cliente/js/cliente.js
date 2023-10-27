// const div_hover_category = document.getElementById('hover-category');
// const button_category = document.getElementById('category-hover-button');
// var class_itens = "absolute -left-8 top-full z-10 mt-3 w-screen max-w-md overflow-hidden rounded-3xl bg-white shadow-lg ring-1 ring-gray-900/5";


// count = 0
// function load_hover(){
//     if(div_hover_category.classList.contains('testDisplayNone')) {
//         div_hover_category.classList.remove('testDisplayNone');
//         div_hover_category.classList.add(class_itens);
//     }
//     count = count + 1;
//     if(count % 2 != 0){
//         div_hover_category.classList.add('testDisplayNone')
//     }
// }

// button_category.addEventListener('click', load_hover);

const icon = document.querySelector('.icon');
const search = document.querySelector('.search');
icon.onclick = function(){
    search.classList.toggle('active')
}

const liElement = document.querySelector('.HeaderHoverFunction');
const invisibleBox = liElement.querySelector('.invisibleBox');

liElement.addEventListener('mouseover', () => {
    invisibleBox.classList.add('visible');
});

liElement.addEventListener('mouseout', (e) => {
    if (!e.relatedTarget || !invisibleBox.contains(e.relatedTarget)) {
        invisibleBox.classList.remove('visible');
    }
});

invisibleBox.addEventListener('mouseover', () => {
    invisibleBox.classList.add('visible');
});

invisibleBox.addEventListener('mouseout', (e) => {
    if (!e.relatedTarget || !liElement.contains(e.relatedTarget)) {
        invisibleBox.classList.remove('visible');
    }
});