const todoForm = document.getElementById('todo-form');
const todoInput = document.getElementById('todo-input');
const todoList = document.getElementById('todo-list');

todoForm.addEventListener('submit', function(event) {
  event.preventDefault();
  
  const todoText = todoInput.value.trim();
  
  if (todoText !== '') {
    const todoItem = createTodoItem(todoText);
    todoList.appendChild(todoItem);
    todoForm.action = "/";
    todoForm.submit();
    
  }
});

function createTodoItem(todoText) {
  const li = document.createElement('li');
  const todoTextSpan = document.createElement('span');
  const deleteButton = document.createElement('button');
  
  todoTextSpan.textContent = todoText;
  
  deleteButton.textContent = 'Delete';
  deleteButton.classList.add('delete-button');
  
  li.appendChild(todoTextSpan);
  li.appendChild(deleteButton);
  
  deleteButton.addEventListener('click', function() {
    li.remove();
  });
  
  li.addEventListener('click', function() {
    li.classList.toggle('completed');
  });
  
  return li;
}
