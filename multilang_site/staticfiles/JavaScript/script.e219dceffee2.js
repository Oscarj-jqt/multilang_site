document.addEventListener("DOMContentLoaded", function() {

    const allButtons = document.querySelectorAll(".searchBtn");
    const searchBar = document.querySelector(".searchBar");
    const searchInput = document.getElementById("searchInput");
    const searchClose = document.getElementById("searchClose"); 

    for (var i = 0; i < allButtons.length; i++) {
        
        allButtons[i].addEventListener("click", function() {
            searchBar.style.visibility = "visible";
            searchBar.classList.add("open");
            this.setAttribute("aria-expanded", "true");
            searchInput.focus();
        });
    }

    searchClose.addEventListener("click", function() {
            searchBar.style.visibility = "hidden";
            searchBar.classList.remove("open");
            this.setAttribute("aria-expanded", "false");
        });

});

//chatbot
$(document).ready(function() {
    $('#chat-form').on('submit', function(event) {
        event.preventDefault();
        const userInput = $('#user-input').val();
        $.ajax({
            url: "{% url 'chatbot' %}",
            method: 'POST',
            data: {
                user_input: userInput,
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success: function(response) {
                $('#chat-response').html(response.response);
            },
            error: function() {
                $('#chat-response').html("An error occurred. Please try again.");
            }
        });
    });
});