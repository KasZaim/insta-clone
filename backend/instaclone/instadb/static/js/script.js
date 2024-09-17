// let posts = [
//     {
//         'profilimg': 'img/Profilbilder/ali-pazani-2613260.jpg',
//         'user': 'JasminTasty',
//         'image': ['img/posts/img1.jpg'],
//         'description': 'Breakfast for Champions,',
//         'location': 'Home',
//         'likes': 2533,
//         'full-description': 'Das Rezept für die Pancakes gibt es in meiner Bio :-)',
//         'date': 'Gestern',
//         'hashtags': '#foodie #lazy',
//         'liked': false,
//         'comments': [
//             {
//                 'user': 'Izzy. I',
//                 'pic': 'img/Profilbilder/pexels-pixabay-415829.jpg',
//                 'comment': 'Yummy '
//             },
//             {
//                 'user': 'Mister Joe',
//                 'pic': 'img/Profilbilder/pexels-anna-nekrashevich-6801642.jpg',
//                 'comment': 'Das sieht Lecker aus'
//             }
//         ]
//     },
//     {
//         'profilimg': 'img/Profilbilder/daniel-xavier-1239288.jpg',
//         'user': 'Fashion_Nova',
//         'image': ['img/posts/img2.jpg', 'img/posts/img3.jpg', 'img/posts/img4.jpg'],
//         'description': 'Photoshoot for the New Brand Prana Luna.',
//         'location': 'Hamburg',
//         'likes': 1521,
//         'full-description': 'Leute checkt die neue Kollektion von Prana Luna for Her ab! Die haben ein paar richtig nice Outfits für euch',
//         'date': 'vor 45 Minuten',
//         'hashtags': '#fashion #instalife #prana',
//         'liked': false,
//         'comments': [
//             {
//                 'user': 'Mister Joe',
//                 'pic': 'img/Profilbilder/pexels-anna-nekrashevich-6801642.jpg',
//                 'comment': 'Slayin that Look !'
//             },
//             {
//                 'user': 'Laura',
//                 'pic': 'img/Profilbilder/daniel-xavier-1239288.jpg',
//                 'comment': 'Nice'
//             }
//         ]
//     },
//     {
//         'profilimg': 'img/Profilbilder/pixabay-38554.jpg',
//         'user': 'Healthy_Recipes',
//         'image': ['img/posts/img5.jpg'],
//         'description': 'Hier haben wir ein High Protein Porridge,',
//         'location': 'LXS Studios GmbH, Köln',
//         'likes': 558,
//         'full-description': 'mit unglaublichen 50gr Protein pro Portion, und dazu schmeckt es einfach fantastisch',
//         'date': 'vor 5 std',
//         'hashtags': '#goodlife #healthylifestyle #fruits',
//         'liked': false,
//         'comments': [
//             {
//                 'user': 'Mister Joe',
//                 'pic': 'img/Profilbilder/pexels-anna-nekrashevich-6801642.jpg',
//                 'comment': 'Das sieht Lecker aus'
//             },
//             {
//                 'user': 'Mister Joe',
//                 'pic': 'img/Profilbilder/pexels-anna-nekrashevich-6801642.jpg',
//                 'comment': 'Das sieht Lecker aus'
//             }
//         ]
//     },
//     {
//         'profilimg': 'img/Profilbilder/pexels-pixabay-413959.jpg',
//         'user': 'Travel_addicted',
//         'image': ['img/posts/img6.jpg'],
//         'description': 'Mal wieder unterwegs,',
//         'location': 'Budapest',
//         'likes': 2685,
//         'full-description': 'diesesmal bin ich in Budapest.. und was soll ich sagen es ist einfach schön hier zu der Jahreszeit!m ',
//         'date': 'vor 10 std',
//         'hashtags': '#travel #vloglifestyle #happy ',
//         'liked': false,
//         'comments': [
//             {
//                 'user': 'Mister Joe',
//                 'pic': 'img/Profilbilder/pexels-anna-nekrashevich-6801642.jpg',
//                 'comment': 'Das sieht Lecker aus'
//             },
//             {
//                 'user': 'Mister Joe',
//                 'pic': 'img/Profilbilder/pexels-anna-nekrashevich-6801642.jpg',
//                 'comment': 'Das sieht Lecker aus'
//             }
//         ]
//     }
// ];

function fetchPosts() {
    fetch('http://127.0.0.1:8000/get_posts/')
        .then(response => response.json())
        .then(posts => {
            renderPosts(posts);
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
        renderComments(i);
    }
}


function renderComments(i){
    let comments = document.getElementById(`comments${i}`);
    let commentsAmount = posts[i].comments.length;
    comments.innerHTML = '';
    for (let k = 0; k < commentsAmount; k++) {
        const comment = posts[i].comments[k]; // Korrektur hier
        comments.innerHTML +=`

            <div><b>${comment.user}</b>: ${comment.comment}</div>`;
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

function gotLiked(i) {
    let image = document.getElementById(`heart${i}`);
    if (posts[i].liked == false) {
        image.src = "img/heart.png";
        posts[i].liked = true;
        ++posts[i].likes;
    } else {
        image.src = "img/love.png";
        posts[i].liked = false;
        --posts[i].likes;
    }
    document.getElementById(`liked${i}`).innerHTML = posts[i].likes;
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









