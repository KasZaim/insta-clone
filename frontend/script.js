
let fetchedPosts = [];
let url = 'http://127.0.0.1:8000';
let isProcessingLike = false;

function fetchPosts() {
    console.log("fetchPosts() wurde aufgerufen");
    fetch(`${url}/get_posts/`)
        .then(response => response.json())
        .then(posts => {
            renderPosts(posts);
            posts.forEach(post => {
                fetchedPosts.push(post)
            });
            console.log(fetchedPosts)
        })
        .catch(error => console.error('Error fetching posts:', error));
}

function renderPosts(posts) {
    let content = document.getElementById('posted');
    content.innerHTML = '';
    for (let i = 0; i < posts.length; i++) {
        const post = posts[i];
        let commentsAmount = post.comments_count;

        content.innerHTML += postsTemplate(i, post, commentsAmount);

        // Carousel wird direkt in postsTemplate gerendert
        renderComments(i, posts);
    }
}


function renderComments(i, posts) {
    let comments = document.getElementById(`comments${i}`);
    let commentsAmount = posts[i].comments.length;
    comments.innerHTML = '';
    for (let k = 0; k < commentsAmount; k++) {
        const comment = posts[i].comments[k]; // Korrektur hier
        comments.innerHTML += `

            <div><b>${comment.user_profile__username}</b>: ${comment.comment_text}</div>`;
    }
}

function readmore(i) {
    let span = document.getElementById(`more${i}`);
    let fullText = document.getElementById(`full-text${i}`);
    let textContainer = document.getElementById(`posted-text-container${i}`);
    span.classList.add('d-none');
    fullText.classList.remove('d-none');
    textContainer.classList.remove('cut-posted-text');
}
function scrollLinks() {
    let scrollableDiv = document.getElementById('horizontal-scroll');
    scrollableDiv.scrollLeft -= 100;
};
function scrollRight() {
    let scrollableDiv = document.getElementById('horizontal-scroll');
    scrollableDiv.scrollLeft += 100;
};


async function renderLikes(event, i) {
    event.preventDefault();  // Verhindere das Neuladen der Seite

    const post = fetchedPosts[i];  // Den spezifischen Post holen
    const response = await fetch(`http://127.0.0.1:8000/toggle_like/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `post_id=${post.id}&user_profile_id=${post.user_profile__id}`
    });
    event.preventDefault();
    const data = await response.json();  // Erhalte die Serverantwort
    if (data.liked) {
        document.getElementById(`heart${i}`).src = "img/heart.png";  
    } else {
        document.getElementById(`heart${i}`).src = "img/love.png";
    }
    document.getElementById(`liked${i}`).innerText = data.likes_count; 
    return false // Like-Zählung aktualisieren
}




function gotLiked(i, data) {
    let image = document.getElementById(`heart${i}`);
    let post = fetchedPosts[i]; // Aktualisiere das richtige Post-Objekt

    if (data.liked) {
        image.src = "img/heart.png"; // Zeige gefülltes Herz, wenn geliked
        post.liked = true;
        post.likes += 1;
    } else {
        image.src = "img/love.png"; // Zeige leeres Herz, wenn nicht geliked
        post.liked = false;
        post.likes -= 1;
    }

    document.getElementById(`liked${i}`).innerHTML = post.likes; // Aktualisiere die Anzahl der Likes
}

//Filters out the user;
function filterNames() {
    let search = document.getElementById('search').value;
    search = search.toLowerCase();
    let content = document.getElementById('posted');
    content.innerHTML = '';
    for (let i = 0; i < posts.length; i++) {
        let post = posts[i];
        if (post.user.toLowerCase().includes(search)) {
            content.innerHTML += postsTemplate(i, post);
        }
    }
}

function enableButton(i) {
    let input = document.getElementById(`comment-input${i}`);
    let commentBtn = document.getElementById(`comment-btn${i}`);
    commentBtn.disabled = !input.value;
    if (commentBtn.disabled == false) {
        commentBtn.style.color = 'darkblue';
    } else {
        commentBtn.style.color = 'gray';
    }
}









