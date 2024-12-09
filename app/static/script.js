const form = document.getElementById('form');
const result = document.getElementById('result');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;

  fetch('/api/users', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ name, email })
  })
  .then((response) => response.json())
  .then((data) => {
    result.innerHTML = `User created successfully! ID: ${data.id}`;
  })
  .catch((error) => {
    result.innerHTML = `Error: ${error.message}`;
  });
});