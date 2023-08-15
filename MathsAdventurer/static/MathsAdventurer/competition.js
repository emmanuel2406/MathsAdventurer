document.addEventListener('DOMContentLoaded',() =>{
    console.log('...loaded...');
    document.querySelectorAll('.add').forEach(button => {
        button.addEventListener('click', () => watchlist_update(button, 1))
    })
    document.querySelectorAll('.remove').forEach(button => {
        button.addEventListener('click', () => watchlist_update(button, 0))
    })
    document.querySelector('.grade-filter').addEventListener("change", grade_filter)
});

function grade_filter(){
    let grade = parseInt(this.options[this.selectedIndex].value);
    console.log(grade);
    document.querySelectorAll('.comp').forEach(div => {
        let  min_grade = parseInt(div.dataset.min_grade);
        let max_grade = parseInt(div.dataset.max_grade);
        if (grade == 0 ){
            div.style.display = 'block';
        }
        else if (min_grade <= grade && grade <= max_grade){
            div.style.display = 'block';
        }
        else{
            div.style.display = 'none';
        }
    })
};
function watchlist_update(button, is_add){
    fetch('/watchlist_update',{
        method :"POST",
        body : JSON.stringify({
            comp_id : button.dataset.id,
            is_add : is_add
        })
    })
    .then(response => response.json())
    .then(result => {
        console.log(result)
        location.reload();
    })
    .catch(err => handleError(err))
};

function handleError(err){
    console.log('There is an error:');
    console.log(err);
}