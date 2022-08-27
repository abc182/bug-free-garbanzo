
const form = document.getElementById('form');
const uname = document.getElementById('n');
const pass = document.getElementById('e');
const repass = document.getElementById('g');

form.addEventListener('submit',e =>{
    e.preventDefault();

    validateInputs();

});
const setError=(element,message)=>
{
    const inputcontrol = element.parentElement;
    const errorDisplay = inputcontrol.querySelector('.error');
    inputcontrol.classList.add('error');
    inputcontrol.classList.remove('success');
    
}
const validateInputs = () =>{
    const unameValue = uname.value.trim();
    const passValue = pass.value.trim();
    const repassValue = repass.value.trim(); 
}
if(unameValue == ''){
    setError(uname,"userid is required");
}
if (pass===''){
    setError(pass,"password is required")
}
