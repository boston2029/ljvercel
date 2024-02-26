const applyButton = document.getElementById('apply');

if (applyButton) {
  applyButton.addEventListener('click', () => {
    let address = prompt('Enter your email address:');
    fetch(`/apply?to=${address}&job=${applyButton.dataset.job}`);
    alert('Thank you for applying to Libit! Please check your email.');
  });
}
