document.addEventListener('DOMContentLoaded',() =>{
    console.log('...loaded...');
    document.querySelectorAll('.status').forEach(select =>{
      select.selectedIndex = select.dataset.index
      select.style.backgroundColor = select.options[select.selectedIndex].style.backgroundColor
    });
    document.querySelectorAll('.status-form').forEach(form =>{
        form.onsubmit = () => save_status(form)
      });
    document.querySelector('.archive-info').addEventListener('click',button =>{
      alert('Milestones dated before this year are automatically archived');
    });
});


function save_status(form){
    select = form.querySelector('.status');
    output = select.selectedIndex;
    fetch('/status_update',{
        method: 'POST',
        body: JSON.stringify({
            milestone_id : form.dataset.id,
            status : output
        })
    })
    .then(response => response.json())
    .then(result => {
        console.log(result)
    })
    .catch(err => handleError(err));
    select.style.backgroundColor = select.options[output].style.backgroundColor
    alert('Status updated.')
    return false;
}

function handleError(err){
    console.log('There is an error:');
    console.log(err);
}

